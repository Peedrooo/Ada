from pydantic import BaseModel

class Discipline(BaseModel):
    name: str
    flow: int
    workload: int = 60
    lab: str = 'comum'

    def __str__(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def set_flow(self, flow: int):
        self.flow = flow

    def set(self):
        self.lab = True

    def set_workload(self, workload: int):
        self.workload = workload

    def get_flow(self) -> int:
        return self.flow

    def is_lab(self) -> bool:
        return self.lab

    def get_workload(self) -> int:
        return self.workload
    
    def __repr__(self) -> str:
        return f"{self.name}-{self.flow}-{self.workload}-{self.lab}"

    def get_all(self) -> dict:
        return {
            'name': self.name,
            'flow': self.flow,
            'lab': self.lab,
            'workload': self.workload
        }
