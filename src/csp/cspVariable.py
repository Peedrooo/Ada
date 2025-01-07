import sys
sys.path.append('../src')
from variable import Variable

class cspVariable(Variable):
    
    def __init__(self, turma):
        super().__init__(None)
        __turma = turma

    def compute_value(self):
        values = []
        for i in range(domain_size):
            values.append(cspValue(self, i))
        return values
    
    def get_turma(self):
        return self.__turma