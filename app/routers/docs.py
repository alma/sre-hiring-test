from fastapi import APIRouter
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from starlette.responses import JSONResponse

from app.config import DESCRIPTION, TITLE, VERSION

router = APIRouter()


@router.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    response = get_swagger_ui_html(
        openapi_url="/openapi.json",
        title=TITLE + " - Swagger UI",
        oauth2_redirect_url="/docs/oauth2-redirect",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )
    return response


@router.get("/redoc", include_in_schema=False)
async def redoc_html():
    response = get_redoc_html(
        openapi_url="/openapi.json",
        title=TITLE + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )
    return response


@router.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    from app.main import app

    response = JSONResponse(
        get_openapi(title=TITLE, version=VERSION, description=DESCRIPTION, routes=app.routes)
    )
    return response
