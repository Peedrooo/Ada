from variable   import variable
from typing import List

class Interface:
    def __init__(self, data:List[variable]):
        self.data = data

    def draw(self):
        for var in self.data:
            local, day, time = var.value
            print(f'Disciplina {var.Class.discipline.name} - Turma {var.Class.id}: Sala {local.name} - Dia {day} - horário {time}')    
