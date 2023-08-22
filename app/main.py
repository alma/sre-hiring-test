from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import DESCRIPTION, TITLE, VERSION
from app.libs.sentry import setup_sentry
from app.routers import convert, docs, pings

app = FastAPI(
    title=TITLE,
    description=DESCRIPTION,
    version=VERSION,
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)

setup_sentry(app)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(docs.router, tags=["documentation"])
app.include_router(pings.router, tags=["ping"])
app.include_router(convert.router, tags=["convert"])
