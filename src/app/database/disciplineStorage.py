import logging
import os
from typing import Dict, List, Optional

from fastapi import HTTPException

from app.database.storage import Storage
from model.discipline import Discipline


class DisciplineStorage(Storage):
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
        with open(path, 'w', encoding='utf-8') as file:
            for discipline in self._storage.values():
                file.write(f"{discipline.name}-{discipline.flow}-"
                           f"{discipline.workload}-{discipline.type}\n")
        logging.info("Saved all disciplines.")

    def load_disciplines(self, path: str) -> None:
        """Carrega todas as disciplinas cadastradas de um arquivo txt."""
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                for line in file:
                    name, flow, workload, type = line.strip().split('-')
                    discipline = Discipline(
                        name=name, flow=flow, 
                        workload=int(workload), 
                        type=type)
                    self.add_discipline(discipline)
            logging.info("Loaded all disciplines.")
        else:
            logging.warning("File not found.")

    def delete_all_disciplines(self, path: str) -> None:
        """Remove todas as disciplinas do armazenamento em memória e do arquivo txt."""
        self._storage.clear()
        if os.path.exists(path):
            os.remove(path)
        logging.info("Deleted all disciplines.")

    def get_all(self) -> Dict[str, Discipline]:
        """Retorna todas as disciplinas armazenadas."""
        return self._storage.values()


discipline_storage = DisciplineStorage()
discipline_storage.load_disciplines('src/data/disciplines.txt')
