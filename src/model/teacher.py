class Teacher:
    def __init__(
            self, name: str,
            discipline: tuple = None,
            prefered_disciplines: list = [],
            possible_disciplines: list = [],
            workload: int = 0,
            director: bool = False,
            coordinator: bool = False
            ):

        self.name = name
        self.discipline = discipline
        self.prefered_disciplines = prefered_disciplines
        self.possible_disciplines = possible_disciplines
        self.workload = workload

        if director:
            self.max_workload = 0

        elif coordinator:
            self.max_workload = 15 * 4

    def __str__(self):
        return self.name

    def set_discipline(self, discipline: tuple):
        self.discipline = discipline

    def set_prefered_disciplines(self, prefered_disciplines: list):
        self.prefered_disciplines = prefered_disciplines

    def set_possible_disciplines(self, possible_disciplines: list):
        self.possible_disciplines = possible_disciplines

    def set_max_workload(self, max_workload: int):
        self.max_workload = max_workload

    def set_workload(self, workload: int):
        self.workload = workload

    def get_discipline(self) -> tuple:
        return self.discipline

    def get_prefered_disciplines(self) -> list:
        return self.prefered_disciplines

    def get_possible_disciplines(self) -> list:
        return self.possible_disciplines

    def get_workload(self) -> int:
        return self.workload

    def get_max_workload(self) -> int:
        return self.max_workload

    def get_all(self) -> dict:
        return {
            'name': self.name,
            'discipline': self.discipline,
            'workload': self.workload,
            'max_workload': self.max_workload
        }
