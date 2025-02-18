from scripts.variable import variable
from typing import List
import pandas as pd
from IPython.display import display

class Interface:
    def __init__(self, data:List[variable]):
        self.data = data

    def draw(self, output_file=None):
        df = pd.DataFrame(columns=['Disciplina', 'Turma', 'Sala', 'Dia', 'Horario'])
        for var in self.data:
            local, day, time = var.value
            nova_linha = pd.DataFrame([{'Disciplina': var.Class.discipline.name, 'Turma': var.Class.id, 'Sala': local.name, 'Dia': day, 'Horario': time}])
            df = pd.concat([df, nova_linha], ignore_index=True)
            # print(f'Disciplina {var.Class.discipline.name} - Turma {var.Class.id}: Sala {local.name} - Dia {day} - horário {time}')
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(df.to_string(index=False))
        else:
            display(df)
