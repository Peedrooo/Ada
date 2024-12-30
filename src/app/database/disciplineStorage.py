from typing import Dict, List, Optional
from fastapi import HTTPException
# from src.model.disciplineDataModel import DisciplineModel
from model.discipline import Discipline
import logging
import os


class DisciplineStorage:
    def __init__(self):
        self._storage: Dict[str, Discipline] = {}

    def add_discipline(self, discipline: Discipline) -> None:
        """Adiciona uma nova disciplina à estrutura de armazenamento."""
        if discipline.name not in self._storage:
            self._storage[discipline.name] = discipline
            logging.info(f"Added discipline: {discipline}")
        else:
            logging.warning(f"Discipline with name '{discipline.name}' already exists.")

    def get_discipline(self, name: str) -> Optional[Discipline]:
        """Recupera uma disciplina pelo nome."""
        discipline = self._storage.get(name)
        if not discipline:
            logging.warning(f"Discipline with name '{name}' not found.")
            raise HTTPException(
                status_code=404,
                detail=f"Discipline with name '{name}' not found."
            )
        logging.info(f"Retrieved discipline: {discipline}")
        return discipline

    def list_disciplines(self) -> List[Dict[str, str]]:
        """Lista todas as disciplinas armazenadas."""
        logging.info(f"Listing all disciplines: {len(self._storage)} found.")
        return [discipline.get_all() for discipline in self._storage.values()]

    def save_disciplines(self, path: str) -> None:
        """Cria um arquivo txt com todas as disciplinas cadastradas."""
        with open(path, 'w') as file:
            for discipline in self._storage.values():
                file.write(f"{discipline.name}-{discipline.flow}-"
                           f"{discipline.workload}-{discipline.lab}\n")
        logging.info("Saved all disciplines.")

    def delete_all_disciplines(self, path: str) -> None:
        """Remove todas as disciplinas do armazenamento em memória e do arquivo txt."""
        self._storage.clear()
        if os.path.exists(path):
            os.remove(path)
        logging.info("Deleted all disciplines.")


discipline_storage = DisciplineStorage()
