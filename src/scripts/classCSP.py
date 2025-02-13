import sys

sys.path.append('./src')

from constraint import constraint
from variable import variable
from typing import List
from model.classrom import Classrom

class classCSP:
    def __init__(self, locals:List[Classrom], days, times, cources, constraint:constraint):
        self.constraints = constraint
        self.variable_list = []
        self.locals = locals
        self.days = days
        self.times = times
        self.cources = cources

    def init_variables(self):
        """
        Gerar as turmas e adicionar varável na lista
        iniciar todas com mesmo domínio
        """
        # Hierarquia de ordenação: dia, horário, local
        domain = [(local, day, horario) for day in self.days for horario in self.times for local in self.locals]
        for cource in self.cources:
            var = variable(cource, domain)
            self.variable_list.append(var)
    
    def sort_variables(self):
        """
        Ordena as turmas por carga horária
        como uma heurística
        """
        self.variable_list = sorted(self.variable_list, key = lambda x: x.Class.discipline.workload, reverse=True)
        # for var in self.variable_list:
            # print(f'{var.Class.discipline.name}, id - {var.Class.id}, part - {var.Class.part}, carga horária: {var.Class.discipline.workload}')
