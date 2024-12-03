class Constraint:
    def variables(self):
        """
        Retorna as variáveis associadas a esta restrição.
        Este método precisa ser implementado por subclasses.
        """
        raise NotImplementedError("O método 'variables' precisa ser implementado.")

    def compute_conflicts(self, value, conflicts):
        """
        Calcula os conflitos associados a um valor.
        Este método precisa ser implementado por todas as subclasses.
        """
        raise NotImplementedError("O método 'compute_conflicts' precisa ser implementado.")

    def unassigned(self, value):
        """
        Método chamado quando um valor é desatribuído.
        Pode ser sobrescrito pelas subclasses.
        """
        pass

    def assigned(self, value):
        """
        Método chamado quando um valor é atribuído.
        Remove valores conflitantes.
        """
        conflicts = set()
        self.compute_conflicts(value, conflicts)
        for conflicting_value in conflicts:
            conflicting_value.variable().unassign()