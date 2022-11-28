from apis.base import api_router
from core.config import settings
from db.base import Base
from db.session import engine
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from webapps.base import api_router as web_app_router


def include_router(app: FastAPI):
    app.include_router(api_router)
    app.include_router(web_app_router)


def configure_static(app: FastAPI):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def create_table():
    Base.metadata.create_all(bind=engine)


def start_application() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app=app)
    configure_static(app=app)
    create_table()
    return app


app = start_application()
