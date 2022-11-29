from fastapi import APIRouter
from webapps.auth import route_login
from webapps.jobs import route_jobs
from webapps.users import route_users

api_router = APIRouter()
api_router.include_router(router=route_jobs.router, prefix="", tags=["job-webapp"])
api_router.include_router(
    router=route_users.router, prefix="/user", tags=["user-webapp"]
)
api_router.include_router(
    router=route_login.router, prefix="/auth", tags=["auth-webapp"]
)
