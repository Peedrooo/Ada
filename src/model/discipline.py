from pydantic import BaseModel


class Discipline(BaseModel):
    name: str
    flow: int
    course: str
    type: str = 'comum'
    workload: int = 60

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

    def set_cource(self, course: str):
        self.course = course
    
    def get_flow(self) -> int:
        return self.flow
    
    def get_workload(self) -> int:
        return self.workload
    
    def get_type(self) -> str:
        return self.type

    def get_cource(self) -> str:
        return self.course

    def gen_code(self) -> str:
        return f"{self.name}-{self.flow}"
    
    def __repr__(self) -> str:
        return f"{self.name}-{self.flow}-{self.workload}-{self.type}-{self.course}"

    def get_all(self) -> dict:
        return {
            'name': self.name,
            'flow': self.flow,
            'type': self.type,
            'workload': self.workload,
            'course': self.course
        }
