from interfaces import TerminatorCondition

class GeneralTerminationCondition:
    def __init__(self, max_iter=-1, timeout=-1, stop_when_complete=False):
        """
        Inicializa as condições de término.
        """
        self.__max_iter = max_iter
        self.__timeout = timeout
        self.__stop_when_complete = stop_when_complete

    def can_continue(self, current_solution):
        """
        Verifica se o processo pode continuar com base nas condições de término.
        """
        # Número máximo de iterações atingido.
        if self.__max_iter >= 0 and current_solution.get_iteration() >= self._max_iter:
            return False

        # Tempo limite atingido.
        if self._timeout >= 0 and current_solution.get_time() > self._timeout:
            return False

        # Verifica se a solução está completa.
        if self.__stop_when_complete:
            return len(current_solution.get_model().unassigned_variables()) > 0

        return True
