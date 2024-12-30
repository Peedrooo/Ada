from typing import Dict, List, Optional
from fastapi import HTTPException
from model.teacher import Teacher
import logging
import os


class TeacherStorage:
    def __init__(self):
        self._storage: Dict[str, Teacher] = {}

    def add_teacher(self, teacher: Teacher) -> None:
        """Adiciona uma nova teacher à estrutura de armazenamento."""
        if teacher.name not in self._storage:
            self._storage[teacher.name] = teacher
            logging.info(f"Added teacher: {teacher}")
        else:
            logging.warning(f"Teacher with name '{teacher.name}' already exists.")

    def get_teacher(self, name: str) -> Optional[Teacher]:
        """Recupera uma teacher pelo nome."""
        teacher = self._storage.get(name)
        if not teacher:
            logging.warning(f"Teacher with name '{name}' not found.")
            raise HTTPException(
                status_code=404,
                detail=f"Teacher with name '{name}' not found."
            )
        logging.info(f"Retrieved teacher: {teacher}")
        return teacher

    def list_teachers(self) -> List[Dict[str, str]]:
        """Lista todas as teachers armazenadas."""
        logging.info(f"Listing all teachers: {len(self._storage)} found.")
        return [teacher.get_all() for teacher in self._storage.values()]

    def save_teachers(self, path: str) -> None:
        """Cria um arquivo txt com todas as teachers cadastradas."""
        with open(path, 'w') as file:
            for teacher in self._storage.values():
                file.write(
                    f"{teacher.name}-{teacher.prefered_disciplines}-"
                    f"{teacher.possible_disciplines}-{teacher.prefered_workload}-"
                    f"{teacher.director}-{teacher.coordinator}-{teacher.max_workload}\n"
                    )
        logging.info("Saved all teachers.")

    def delete_all_teachers(self, path: str) -> None:
        """Remove todas as teachers do armazenamento em memória e do arquivo txt."""
        self._storage.clear()
        if os.path.exists(path):
            os.remove(path)
        logging.info("Deleted all teachers.")


teacher_storage = TeacherStorage()
