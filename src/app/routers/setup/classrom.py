import logging

from app.database.classromStorage import classrom_storage
from fastapi import APIRouter, status, Response
from model.classrom import Classrom
from typing import List

router = APIRouter()

@router.post("/setup/classrom", status_code=status.HTTP_201_CREATED, tags=["Setup"])
def create_classroms(classrooms: List[Classrom], response: Response):
    try:
        for classrom in classrooms:
            classrom_storage.add_classrom(classrom)
        response.status_code = status.HTTP_201_CREATED
        logging.info("Created new classroms")
        classrom_storage.save_classroms('./src/data/classroms.txt')
        return {
            "message": f"Classroms created successfully"
            }
    except Exception as e:
        logging.error(f"Error creating a new classrom: {e}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Internal Server Error"}

@router.get("/setup/classrom", tags=["Setup"])
def list_classroms():
    try:
        classroms = classrom_storage.list_classroms()
        logging.info("Listed all classroms")
        return classroms

    except Exception as e:
        logging.error(f"Error listing classroms: {e}")
        return {"message": "Internal Server Error"}
    
@router.delete("/setup/classrom/all", status_code=status.HTTP_204_NO_CONTENT, tags=["Setup"])
def delete_classrom( response: Response):
    try:
        classrom_storage.delete_all_classroms('./src/data/classroms.txt')
        classrom_storage._storage.clear()
        response.status_code = status.HTTP_204_NO_CONTENT
        logging.info("Deleted all classroms")
        return {
            "message": "Classroms deleted successfully"
        }
    except Exception as e:
        logging.error(f"Error deleting classrom: {e}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Internal Server Error"}