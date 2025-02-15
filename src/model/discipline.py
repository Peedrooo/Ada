from pydantic import BaseModel

class Discipline(BaseModel):
    name: str
    flow: int
    workload: int = 60
    type: str = 'comum'

    def __str__(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def set_flow(self, flow: int):
        self.flow = flow

    def set_workload(self, workload: int):
        self.workload = workload

    def set_type(self, type: str):
        self.type = type

    def get_flow(self) -> int:
        return self.flow
    
    def get_workload(self) -> int:
        return self.workload
    
    def get_type(self) -> str:
        return self.type

    def gen_code(self) -> str:
        return f"{self.name}-{self.flow}"
    
    def __repr__(self) -> str:
        return f"{self.name}-{self.flow}-{self.workload}-{self.type}"

    def get_all(self) -> dict:
        return {
            'name': self.name,
            'flow': self.flow,
            'type': self.type,
            'workload': self.workload
        }
