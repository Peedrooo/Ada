from pydantic import BaseModel
from model.discipline import Discipline
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.database.disciplineStorage import DisciplineStorage


class ClassDemand(BaseModel):
    discipline: Discipline | str
    students: int
    turma_size: int = 0
    id: int = 0
    part: int = 0

    def recover_discipline(self):
        disciplineStorage = DisciplineStorage()
        disciplineStorage.load_disciplines('src/data/disciplines.txt')
        self.discipline = disciplineStorage.get_discipline(self.discipline)
        return self
    
    def get_all(self) -> dict:
        return {
            'discipline': self.discipline,
            'students': self.students
        }
        
    def __lt__(self, other):
        return self.students < other.students  # Compara pelo número de alunos

    def __str__(self):
        return (f"Discipline: {self.discipline}, Students: {self.students}")
    

if __name__ == '__main__':
    classDemand = ClassDemand(discipline='APC', students=30)
    classDemand.recover_discipline()
    print(classDemand)