from discipline import Discipline


class ClassDemand():
    def __init__(
        self, discipline: Discipline,
        students: int
            ) -> None:

        self.discipline = discipline
        self.students = students
    
    def __repr__(self):
        return (self.discipline.name, self.students)
