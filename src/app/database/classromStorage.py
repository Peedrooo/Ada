from typing import Dict, List, Optional
from src.model.classrom import Classrom
from fastapi import HTTPException
import logging
import os


class ClassromStorage:
    def __init__(self):
        self._storage: Dict[str, Classrom] = {}

    def add_classrom(self, classrom: Classrom) -> None:
        """Adiciona uma nova sala à estrutura de armazenamento."""
        if classrom.name not in self._storage:
            self._storage[classrom.name] = classrom
            logging.info(f"Added classrom: {classrom}")
        else:
            logging.warning(f"Classrom with name '{classrom.name}' already exists.")

    def get_classrom(self, name: str) -> Optional[Classrom]:
        """Recupera uma sala pelo nome."""
        classrom = self._storage.get(name)
        if not classrom:
            logging.warning(f"Classrom with name '{name}' not found.")
            raise HTTPException(
                status_code=404,
                detail=f"Classrom with name '{name}' not found."
            )
        logging.info(f"Retrieved classrom: {classrom}")
        return classrom

    def list_classroms(self) -> List[Dict[str, str]]:
        """Lista todas as salas armazenadas."""
        logging.info(f"Listing all classroms: {len(self._storage)} found.")
        return [classrom.get_all() for classrom in self._storage.values()]

    def save_classroms(self, path) -> None:
        """Cria um txt com todas as salas cadastradas."""
        with open(path, 'w') as file:
            for classrom in self._storage.values():
                file.write(f"{classrom.name} - {classrom.capacity} - {classrom.type}\n")
        logging.info("Saved all classroms.")
    
    def delete_all_classroms(self, path) -> None:
        """Remove todas as salas do armazenamento em memória e txt."""
        self._storage.clear()
        if os.path.exists(path):
            os.remove(path)
        logging.info("Deleted all classroms.")


classrom_storage = ClassromStorage()
