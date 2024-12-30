import logging

from app.database.disciplineStorage import discipline_storage
from fastapi import APIRouter, status, Response
from model.discipline import Discipline
from typing import List

router = APIRouter()

@router.post("/setup/discipline", status_code=status.HTTP_201_CREATED, tags=["Setup"])
def create_disciplines(disciplines: List[Discipline], response: Response):
    try:
        for discipline in disciplines:
            discipline_storage.add_discipline(discipline)
        response.status_code = status.HTTP_201_CREATED
        logging.info("Created new disciplines")
        discipline_storage.save_disciplines('./src/data/disciplines.txt')
        return {
            "message": f"disciplines created successfully"
            }
    except Exception as e:
        logging.error(f"Error creating a new discipline: {e}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Internal Server Error"}

@router.get("/setup/discipline", tags=["Setup"])
def list_disciplines():
    try:
        disciplines = discipline_storage.list_disciplines()
        logging.info("Listed all disciplines")
        return disciplines

    except Exception as e:
        logging.error(f"Error listing disciplines: {e}")
        return {"message": "Internal Server Error"}
    
@router.delete("/setup/discipline/all", status_code=status.HTTP_204_NO_CONTENT, tags=["Setup"])
def delete_classrom( response: Response):
    try:
        discipline_storage.delete_all_disciplines('./src/data/disciplines.txt')
        discipline_storage._storage.clear()
        response.status_code = status.HTTP_204_NO_CONTENT
        logging.info("Deleted all disciplines")
        return {
            "message": "disciplines deleted successfully"
        }
    except Exception as e:
        logging.error(f"Error deleting discipline: {e}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Internal Server Error"}