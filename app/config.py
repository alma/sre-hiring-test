from pydantic import BaseSettings

TITLE = "Image to PDF converter"
VERSION = "1.0.0"
DESCRIPTION = "Allows to upload and convert images to PDF format."


class Settings(BaseSettings):
    """Application settings, read from environment variables.

    According to https://fastapi.tiangolo.com/advanced/settings/#pydantic-settings

        Pydantic will read the environment variables in a case-insensitive way, so,
        an upper-case variable APP_NAME will still be read for the attribute app_name.
    """

    # PROJECT_ID, as defined by Google Cloud Platform
    project_id: str

    # SENTRY_DSN, to retrieve from Sentry project
    sentry_dsn: str

    # PDF_BUCKET, where to store the converted images files
    pdf_bucket: str


settings = Settings()
