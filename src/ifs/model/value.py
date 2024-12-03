class Value:
    def __init__(self):
        self._variable = None
        self._iteration_assigned = None
        self._iteration_unassigned = None

    def variable(self):
        """
        Retorna a variável associada.
        """
        return self._variable

    def set_variable(self, variable):
        """
        Define a variável associada.
        """
        self._variable = variable

    def assigned(self, iteration):
        """
        Define o momento em que o valor foi atribuído.
        """
        self._iteration_assigned = iteration

    def unassigned(self, iteration):
        """
        Define o momento em que o valor foi desatribuído.
        """
        self._iteration_unassigned = iteration

    def value_equals(self, value):
        """
        Compara o valor atual com outro valor.
        """
        if not isinstance(value, Value):
            return False
        return self.to_int() == value.to_int()

    def to_int(self):
        """
        Converte o valor para um inteiro.
        """
        if self._variable is None:
            raise ValueError("Variable is not set.")
        return int(self._variable)
