import logging

from app.database.classromStorage import classrom_storage
from fastapi import APIRouter, status, Response
from model.classDemand import ClassDemand
from typing import List

router = APIRouter()

@router.post("/run/start", status_code=status.HTTP_201_CREATED, tags=["Run"])
def start_classroms(demand: List[ClassDemand], response: Response):
    try:
        for classrom in demand:
            
            classrom_storage.add_classrom(classrom)
        response.status_code = status.HTTP_201_CREATED
        logging.info("Started new classroms")
        classrom_storage.save_classroms('./src/data/classroms.txt')
        return {
            "message": f"Classroms started successfully"
            }
    except Exception as e:
        logging.error(f"Error starting a new classrom: {e}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Internal Server Error"}
