from scripts.variable import variable
from typing import List
import pandas as pd
from IPython.display import display

class Interface:
    def __init__(self, data:List[variable]):
        self.data = data

    def draw(self):
        df = pd.DataFrame(columns=['Disciplina', 'Turma', 'Sala', 'Dia', 'Horario'])
        for var in self.data:
            local, day, time = var.value
            nova_linha = pd.DataFrame([{'Disciplina': var.Class.discipline.name, 'Turma': var.Class.id, 'Sala': local.name, 'Dia': day, 'Horario': time}])
            df = pd.concat([df, nova_linha], ignore_index=True)
            # print(f'Disciplina {var.Class.discipline.name} - Turma {var.Class.id}: Sala {local.name} - Dia {day} - horário {time}')
        display(df)    
