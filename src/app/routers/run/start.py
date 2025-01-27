import logging

from app.database.classDemandStorage import class_demand_storage
from fastapi import APIRouter, status, Response
from model.classDemand import ClassDemand
from typing import List

router = APIRouter()

@router.post("/run/start", status_code=status.HTTP_201_CREATED, tags=["Run"])
def start_classroms(demand: List[ClassDemand], response: Response):
    try:
        for classrom in demand:
            class_demand_storage.add_class_demand(classrom.recover_discipline())
        response.status_code = status.HTTP_201_CREATED
        logging.info("Started new classroms")
        class_demand_storage.save_class_demands('./src/data/classroms-demand.txt')
        return {
            "message": f"Classroms started successfully"
            }
    except Exception as e:
        logging.error(f"Error starting a new classrom: {e}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Internal Server Error"}
