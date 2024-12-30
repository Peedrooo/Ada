from pydantic import BaseModel


class Teacher(BaseModel):
    name: str
    prefered_disciplines: list = []
    possible_disciplines: list = []
    prefered_workload: int = 0
    director: bool = False
    coordinator: bool = False
    max_workload: int = 0

    if director:
        max_workload = 0

    elif coordinator:
        max_workload = 15 * 4

    def __str__(self):
        return self.name

    def set_prefered_disciplines(self, prefered_disciplines: list):
        self.prefered_disciplines = prefered_disciplines

    def set_possible_disciplines(self, possible_disciplines: list):
        self.possible_disciplines = possible_disciplines

    def set_max_workload(self, max_workload: int):
        self.max_workload = max_workload

    def set_workload(self, prefered_workload: int):
        if prefered_workload > self.max_workload:
            raise ValueError(f"Workload is greater than max workload")
        self.prefered_workload = prefered_workload

    def get_prefered_disciplines(self) -> list:
        return self.prefered_disciplines

    def get_possible_disciplines(self) -> list:
        return self.possible_disciplines

    def get_workload(self) -> int:
        return self.prefered_workload

    def get_max_workload(self) -> int:
        return self.max_workload

    def get_all(self) -> dict:
        return {
            'name': self.name,
            'possible_disciplines': self.possible_disciplines,
            'prefered_workload': self.prefered_workload,
            'max_workload': self.max_workload
        }
