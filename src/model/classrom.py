from pydantic import BaseModel


class Classrom(BaseModel):
    name: str
    capacity: int
    type: str


    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"{self.name} - {self.capacity} - {self.type}"
    
    def get_name(self) -> str:
        return self.name
    
    def get_capacity(self) -> int:
        return self.capacity
    
    def get_type(self) -> str:
        return self.type
    
    def get_all(self) -> dict:
        return {
            'name': self.name,
            'capacity': self.capacity,
            'type': self.type
        }
