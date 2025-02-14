from typing import Dict, List, Optional
from model.classDemand import ClassDemand
from fastapi import HTTPException
from app.database.storage import Storage
import logging
import os


class ClassDemandStorage(Storage):
    def __init__(self):
        self._storage: Dict[str, ClassDemand] = {}

    def add_class_demand(self, class_demand: ClassDemand) -> None:
        """Adiciona uma nova demanda de sala à estrutura de armazenamento."""
        if class_demand.discipline.name not in self._storage:
            self._storage[class_demand.discipline.name] = class_demand
            logging.info(f"Added class demand: {class_demand}")
        else:
            logging.warning(f"Class demand with name '{class_demand.discipline}' already exists.")

    def get_class_demand(self, name: str) -> Optional[ClassDemand]:
        """Recupera uma demanda de sala pelo nome."""
        class_demand = self._storage.get(name)
        if not class_demand:
            logging.warning(f"Class demand with name '{name}' not found.")
            raise HTTPException(
                status_code=404,
                detail=f"Class demand with name '{name}' not found."
            )
        logging.info(f"Retrieved class demand: {class_demand}")
        return class_demand

    def list_class_demands(self) -> List[Dict[str, str]]:
        """Lista todas as demandas de sala armazenadas."""
        logging.info(f"Listing all class demands: {len(self._storage)} found.")
        return [class_demand.get_all() for class_demand in self._storage.values()]

    def return_class_demands(self) -> List[ClassDemand]:
        """Retorna todas as demandas de sala armazenadas."""
        logging.info(f"Returning all class demands: {len(self._storage)} found.")
        return [class_demand for class_demand in self._storage.values()]

    def save_class_demands(self, path) -> None:
        """Cria um txt com todas as demandas de sala cadastradas."""
        with open(path, 'w', encoding='utf-8') as file:
            for class_demand in self._storage.values():
                file.write(f"{class_demand.discipline.name}-{class_demand.students}\n")
        logging.info("Saved all class demands.")

    def load_class_demands(self, path) -> None:
        """Carrega todas as demandas de sala cadastradas de um txt."""
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                for line in file:
                    name, capacity = line.strip().split('-')
                    class_demand = ClassDemand(
                        discipline=name,
                        students=int(capacity) 
                        )
                    class_demand.recover_discipline()
                    self.add_class_demand(class_demand)
            logging.info("Loaded all class demands.")
        else:
            logging.warning("File not found.")
    
    def delete_all_class_demands(self, path) -> None:
        """Remove todas as demandas de sala do armazenamento em memória e txt."""
        self._storage.clear()
        if os.path.exists(path):
            os.remove(path)
        logging.info("Deleted all class demands.")


class_demand_storage = ClassDemandStorage()
class_demand_storage.load_class_demands('src/data/classroms-demand.txt')