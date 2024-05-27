from discipline import Discipline
from teacher import Teacher


class Class():
    def __init__(
        self, discipline: Discipline,
        teacher: Teacher,
        students: int
            ) -> None:

        self.discipline = discipline
        self.teacher = teacher
        self.students = students
