from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.general_pages.route_homepage import general_pages_router
from db.session import engine
from db.base import Base
from apis.base import api_router


def include_router(app: FastAPI):
  app.include_router(api_router)


def configure_static(app: FastAPI):
  app.mount("/static", StaticFiles(directory="static"), name="static")


def create_table():
  Base.metadata.create_all(bind=engine)


def start_application() -> FastAPI:
  app = FastAPI(
    title=settings.PROJECT_NAME, 
    version=settings.PROJECT_VERSION
  )
  include_router(app=app)
  configure_static(app=app)
  create_table()
  return app


app = start_application()

