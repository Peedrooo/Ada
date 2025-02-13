from typing import Dict, List, Optional
from model.classrom import Classrom
from fastapi import HTTPException
from app.database.storage import Storage
from model.local import Local
import logging
import os


class ClassromStorage(Storage):
    def __init__(self):
        self._storage: Dict[str, Classrom] = {}
        self._storage_local: Dict[str, Local] = {}

    def add_classrom(self, classrom: Classrom) -> None:
        """Adiciona uma nova sala à estrutura de armazenamento."""
        if classrom.name not in self._storage:
            self._storage[classrom.name] = classrom
            logging.info(f"Added classrom: {classrom}")
        else:
            logging.warning(f"Classrom with name '{classrom.name}' already exists.")
    
    def add_local(self, local: Local) -> None:
        """Adiciona um novo local à estrutura de armazenamento."""
        if local.name not in self._storage_local:
            self._storage_local[local.name] = local
            logging.info(f"Added local: {local}")
        else:
            logging.warning(f"Local with name '{local.name}' already exists.")

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
    
    def list_classroms(self) -> List[Classrom]:
        """Lista todas as salas armazenadas."""
        logging.info(f"Listing all classroms: {len(self._storage)} found.")
        return [classrom for classrom in self._storage.values()]

    def list_locals(self) -> List[Local]:
        """Lista todos os locais armazenados."""
        logging.info(f"Listing all locals: {len(self._storage_local)} found.")
        return [local for local in self._storage_local.values()]

    def save_classroms(self, path) -> None:
        """Cria um txt com todas as salas cadastradas."""
        with open(path, 'w') as file:
            for classrom in self._storage.values():
                file.write(f"{classrom.name}-{classrom.capacity}-{classrom.type}\n")
        logging.info("Saved all classroms.")

    def load_classroms(self, path) -> None:
        """Carrega todas as salas cadastradas de um txt."""
        if os.path.exists(path):
            with open(path, 'r') as file:
                for line in file:
                    name, capacity, type = line.strip().split('-')
                    classrom = Classrom(
                        name=name,
                        capacity=int(capacity), 
                        type=type)
                    local = Local(
                        name=name,
                        lab=type,
                        supported_load = int(capacity)
                        )
                    self.add_local(local)
                    self.add_classrom(classrom)
            logging.info("Loaded all classroms.")
        else:
            logging.warning("File not found.")
        
        ### Adicionado para carregar os locais
    
    def delete_all_classroms(self, path) -> None:
        """Remove todas as salas do armazenamento em memória e txt."""
        self._storage.clear()
        if os.path.exists(path):
            os.remove(path)
        logging.info("Deleted all classroms.")


classrom_storage = ClassromStorage()
classrom_storage.load_classroms('src/data/classroms.txt')
