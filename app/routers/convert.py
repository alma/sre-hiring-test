import uuid
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory

import httpx
import img2pdf
from fastapi import APIRouter, HTTPException
from google.cloud import storage
from PIL import Image
from pydantic import BaseModel

from app.config import settings

router = APIRouter()


class ImageParameters(BaseModel):
    source_url: str


@router.post("/image_to_pdf")
async def convert_image_to_pdf(image_params: ImageParameters):
    """
    Converts PNG image files to PDF.

    The image will we downloaded then converted to PDF and stored in
    a Google Cloud Storage bucket.
    The call will, then, return the url of the converted PDF file, in the bucket.
    """
    async with httpx.AsyncClient() as client:
        image_result = await client.get(image_params.source_url)

    if image_result.headers.get("content-type") != "image/png":
        raise HTTPException(status_code=412, detail="Invalid file type")

    with TemporaryDirectory() as temp_dir:
        image = Image.open(BytesIO(image_result.content))
        # img2pdf does not support images with transparency. So, remove alpha channel from image.
        image = image.convert("RGB")
        image_bytes = BytesIO()
        image.save(image_bytes, "PNG")

        image_bytes.seek(0)
        dest_filepath = Path(temp_dir) / "dest.pdf"
        with open(dest_filepath, "wb") as dest:
            dest.write(img2pdf.convert(image_bytes))

        storage_client = storage.Client()
        bucket = storage_client.bucket(settings.pdf_bucket)
        blob = bucket.blob(f"{str(uuid.uuid4())}.pdf")
        blob.upload_from_filename(dest_filepath)
        blob.make_public()

    return {
        "source_url": image_params.source_url,
        "converted_url": blob.public_url,
    }
