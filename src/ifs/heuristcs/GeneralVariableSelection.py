from interfaces import VariableSelection
import random

class GeneralVariableSelection(VariableSelection):
    def select_variable(self, solution):
        """
        Seleciona uma variável da solução. Se houver variáveis não atribuídas,
        escolhe aleatoriamente entre elas; caso contrário, escolhe entre as atribuídas.
        """
        unassigned_variables = solution.get_model().unassigned_variables()
        if unassigned_variables:
            return random.choice(unassigned_variables)
        else:
            assigned_variables = solution.get_model().assigned_variables()
            return random.choice(assigned_variables)
