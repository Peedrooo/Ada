import logging

from app.database.teacherStorage import teacher_storage
from fastapi import APIRouter, status, Response
from model.teacher import Teacher
from typing import List

router = APIRouter()

@router.post("/setup/teacher", status_code=status.HTTP_201_CREATED, tags=["Setup"])
def create_teachers(teachers: List[Teacher], response: Response):
    try:
        for teacher in teachers:
            teacher_storage.add_teacher(teacher)
        response.status_code = status.HTTP_201_CREATED
        logging.info("Created new teachers")
        teacher_storage.save_teachers('./src/data/teachers.txt')
        return {
            "message": f"teachers created successfully"
            }
    except Exception as e:
        logging.error(f"Error creating a new teacher: {e}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Internal Server Error"}

@router.get("/setup/teacher", tags=["Setup"])
def list_teachers():
    try:
        teachers = teacher_storage.list_teachers()
        logging.info("Listed all teachers")
        return teachers

    except Exception as e:
        logging.error(f"Error listing teachers: {e}")
        return {"message": "Internal Server Error"}
    
@router.delete("/setup/teacher/all", status_code=status.HTTP_204_NO_CONTENT, tags=["Setup"])
def delete_classrom( response: Response):
    try:
        teacher_storage.delete_all_teachers('./src/data/teachers.txt')
        teacher_storage._storage.clear()
        response.status_code = status.HTTP_204_NO_CONTENT
        logging.info("Deleted all teachers")
        return {
            "message": "teachers deleted successfully"
        }
    except Exception as e:
        logging.error(f"Error deleting teacher: {e}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Internal Server Error"}