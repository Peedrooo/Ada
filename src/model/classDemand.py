from pydantic import BaseModel
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.database.disciplineStorage import DisciplineStorage


class ClassDemand(BaseModel):
    discipline: str
    students: int

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
    
    def __str__(self):
        return (f"Discipline: {self.discipline}, Students: {self.students}")
    

if __name__ == '__main__':
    classDemand = ClassDemand(discipline='APC', students=30)
    classDemand.recover_discipline()
    print(classDemand)