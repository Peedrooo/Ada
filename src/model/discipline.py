class Discipline:
    def __init__(
            self, name: str,
            flow: int,
            workload: int = 60,
            lab: bool = False
            ):

        self.name = name
        self.flow = flow
        self.lab = lab
        self.workload = workload

    def __str__(self):
        return self.name

    def set_flow(self, flow: int):
        self.flow = flow

    def set_lab(self):
        self.lab = True

    def set_workload(self, workload: int):
        self.workload = workload

    def get_flow(self) -> int:
        return self.flow

    def is_lab(self) -> bool:
        return self.lab

    def get_workload(self) -> int:
        return self.workload

    def get_all(self) -> dict:
        return {
            'name': self.name,
            'flow': self.flow,
            'lab': self.lab,
            'workload': self.workload
        }
