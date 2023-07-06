"""Main app module"""
from logging import getLogger

from fastapi import FastAPI
from uvicorn import run

from app.endpoints import list_of_routes
from app.config.default import DefaultSettings as settings

logger = getLogger(__name__)


def bind_routes(application: FastAPI, setting: settings) -> None:
    """
    Bind all routes to application.
    """
    for route in list_of_routes:
        application.include_router(route, prefix=setting.PATH_PREFIX)


def get_app() -> FastAPI:
    """
    Creates application and all dependable objects.
    """
    description = "Микросервис, реализующий возможность укорачивать ссылки."

    tags_metadata = [
        {
            "name": "Url",
            "description": "Manage urls: make them shorter and redirect to long version.",
        },
        {
            "name": "Health check",
            "description": "API health check.",
        },
    ]

    application = FastAPI(
        title="Windy Test app",
        description=description,
        docs_url="/swagger",
        openapi_url="/openapi",
        version="1.0.0",
        openapi_tags=tags_metadata,
    )
    bind_routes(application, settings())
    application.state.settings = settings
    return application


app = get_app()

if __name__ == "__main__":
    run(
        "app.main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=True,
        log_level="debug",
    )
