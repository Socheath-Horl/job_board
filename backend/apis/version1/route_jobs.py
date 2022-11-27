from typing import List

from apis.version1.route_login import get_current_user_from_token
from db.models.user import User
from db.repository.job import create_new_job
from db.repository.job import delete_job_by_id
from db.repository.job import list_jobs
from db.repository.job import retreive_job
from db.repository.job import update_job_by_id
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.job import JobCreate
from schemas.job import ShowJob
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/", response_model=ShowJob)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    job = create_new_job(job=job, db=db, owner_id=current_user.id)
    return job


@router.get(
    "/{id}", response_model=ShowJob
)  # if we keep just "{id}" . it would stat catching all routes
def read_job(id: int, db: Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with this id {id} does not exist",
        )

    return job


@router.get("/", response_model=List[ShowJob])
def read_jobs(db: Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return jobs


@router.put("/{id}")
def update_job(
    id: int,
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    message = update_job_by_id(id=id, job=job, db=db, owner_id=current_user.id)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id {id} not found"
        )
    return {"msg": "Successfully updated data."}


@router.delete("/{id}")
def delete_job(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    message = delete_job_by_id(id=id, owner_id=current_user.id, db=db)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id {id} not found"
        )
    return {"msg": "Successfully deleted."}
