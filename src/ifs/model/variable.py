class Variable:
    def __init__(self):
        self.i_assignment: Optional[Value] = None  # Valor atribuído
        self.i_initial_assignment: Optional[Value] = None  # Valor inicial (MPP)
        self.i_best_assignment: Optional[Value] = None  # Melhor valor atribuído
        self.i_constraints: list[Constraint] = []  # Restrições que contêm esta variável

    def get_values(self):
        """
        Retorna o domínio da variável.
        (Deve ser implementado conforme necessário.)
        """
        raise NotImplementedError("O método get_values deve ser implementado.")

    def unassign(self):
        """
        Desatribui o valor atual da variável e atualiza as restrições associadas.
        """
        old_value = self.i_assignment
        self.i_assignment = None
        for constraint in self.i_constraints:
            constraint.unassigned(self, old_value)

    def assign(self, value):
        """
        Atribui um valor à variável e atualiza as restrições associadas.
        """
        if self.i_assignment is not None:
            self.unassign()
        old_value = self.i_assignment  # Armazena o valor atual antes da nova atribuição
        self.i_assignment = value
        for constraint in self.i_constraints:
            constraint.assigned(self, old_value)

