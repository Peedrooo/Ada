from constraint import constraint
from variable import variable
class classCSP:
    def __init__(self, locals, days, times, cources):
        self.constraints
        self.variable_list = []

    def init_variables(self):
        """
        Gerar as turmas e adicionar varável na lista
        iniciar todas com mesmo domínio
        """
        # Hierarquia de ordenação: dia, horário, local
        domain = [(local, day, horario) for day in self.days for horario in self.times for local in locals]
        for cource in self.cources:
            var = variable(cource, domain)
            self.variable_list.append(var)

    def init_constraint(self):
        self.constraints = constraint()