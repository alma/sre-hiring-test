import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from app.config import settings


def setup_sentry(app):
    """Sets-up Sentry for the FastAPI application passed as argument."""
    if not settings.sentry_dsn:
        return

    sentry_sdk.init(dsn=settings.sentry_dsn)

    app.add_middleware(SentryAsgiMiddleware)
