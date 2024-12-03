from interfaces import SolutionComparator

class GeneralSolutionComparator(SolutionComparator):
    def is_better_than_best_solution(self, current_solution):
        """
        Compara a solução atual com a melhor solução armazenada para determinar se é melhor.
        """
        if current_solution.get_best_info() is None:
            # Não há melhor solução salva ainda
            return True

        # Obtém as variáveis não atribuídas
        current_unassigned = len(current_solution.get_model().unassigned_variables())
        best_unassigned = current_solution.get_model().get_best_unassigned_variables()

        if best_unassigned != current_unassigned:
            return best_unassigned > current_unassigned

        # Compara os valores totais
        current_value = current_solution.get_model().get_total_value()
        best_value = current_solution.get_best_value()

        return current_value < best_value