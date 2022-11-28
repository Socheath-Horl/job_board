from fastapi import APIRouter
from webapps.jobs import route_jobs


api_router = APIRouter()
api_router.include_router(router=route_jobs.router, prefix="", tags=["job-webapp"])
api_router.include_router(router=route_jobs.router, prefix="/jobs", tags=["job-webapp"])
