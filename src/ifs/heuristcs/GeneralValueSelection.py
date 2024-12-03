from interfaces import ValueSelection
import random

class GeneralValueSelection(ValueSelection):
    def __init__(self):
        """
        Inicializa as variáveis.
        """
        self.__i_random_walk_prob = 0.0
        self.__i_weight_conflicts = 1.0
        self.__i_weight_value = 0.0 
        self.__i_tabu_size = 0 
        self.__i_tabu = []
        self.__i_tabu_pos = 0
        self.__i_mpp = False
        self.__i_initial_selection_prob = 0.0
        self.__i_mpp_limit = -1
        self.__i_weight_delta_initial_assignment = 0.0
        self.__i_stat = None
        self.__i_weight_weighted_conflicts = 0.0
        self.__i_mac_propagation = None
        self.__i_allow_no_good = False
    
    def select_Value(self, solution, selected_variable):

        # mpp 
        if self.__i_mpp and selected_variable.get_initial_assignment() is not None:
            # Minimal perturbation problem
            if not solution.get_model().unassigned_variables():
                # Solução completa - diminui o limit MPP
                if len(solution.get_model().perturb_variables()) <= self.__i_mpp_limit:
                    self.__i_mpp_limit = len(solution.get_model().perturb_variables()) - 1

            if self.__i_mpp_limit >= 0 and len(solution.get_model().perturb_variables()) > self__i_mpp_limit:
                # Limite MPP atingido - valor inicial deve ser atribuido
                return selected_variable.get_initial_assignment()
            if random.random() <= self.__i_initial_selection_prob
                # Valor inicial selecionado, dada uma probabilidade 
                return selected_variable.get_initial_assignment()
        # End-MPP

        values = selected_variable.values()

        if random.random() <= self.__i_random_walk_prob:
            # Random walk
            return random.choice(values)

        if self.__i_mac_propagation is not None:
            # MAC: Seleciona um dos valores não removidos
            good_values = self.__i_mac_propagation.good_values(selected_variable)

            if good_values:
                values = list(good_values)
            elif not self.__i_allow_no_good
                # Todos os valores foram removidos, impossível escolher um valor removido
                return None

        # Valores com menor soma de pesos
        best_value = []
        best_weighted_sum = 0.0

        # Passa por todos os valores
        for value in values:
            if value in self.tabu_list:
                # Valor está na tabu-list
                continue

            if value == selected_variable.get_assignment():
                # Pula valor idêntico ao valor atribuido à vairável
                continue
            
            # Valores conflitantes
            conflicts = solution.get_model().conflict_values(value)

            weighted_conflicts = 0.0 # CBS
            if self.__i_stat is not None:
                # Provavelmente não funciona pesquisar o que é count_removals
                weight_conflicts = self.__i_stat.count_removals(solution.get_iteration(), conflicts, value) 

            # MPP: Diferenças nas atribuições iniciais
            delta_initial_assignments = 0
            if self.__i_mpp:
                # Passa por todos os conflitos
                for conflict_value in conflicts
                    if conflict_value.variable().get_initial_assignment() is not None:
                        # Não atribuido a um vlaor inicial -> bom para desatribuição
                        delta_initial_assignments -= 1
                
                if value == selected_variable.get_initial_assignment():
                    # Valor é diferente do inicial -> valor ruim para atribuição
                    delta_initial_assignments += 1

                if __i_mpp_limit >= 0 and (len(solution.get_model().perturb_variables) + delta_initial_assignments) > __i_mpp_limit:
                    # Atribuição excede o limite MPP
                    continue
                
                # Soma de pesos de vários critérios
                weighted_sum = (
                    self.__i_weight_delta_initial_assignment * delta_initial_assignments +
                    self.__i_weight_weighted_conflicts * weight_conflicts +
                    self.__i_weight_conflicts * len(conflicts) +
                    self.__i_weight_value * value.to_int() +
                )

                # Salva melhores valores
                if best_value or best_weighted_sum > weighted_sum:
                    best_weighted_sum = weighted_sum
                    best_values = [value]
                elif best_weighted_sum == weighted_sum:
                    best_values.append(value)
        # Fim do for sobre todos os valores

        selected_value = random.choice(best_values)
        if select_value:
            # Se não houver melhor valor, seleciona um aleatório
            selected_value = random.choice(values)
        
        # Atualiza tabu_list
        if self.__i_tabu:
            if len(self.__i_tabu) == self.__i_tabu_pos:
                self.__i_tabu.append(selected_value)
            else:
                self.__i_tabu[self.__i_tabu_pos] = selected_value
            self.__i_tabu_pos = (self.__i_tabu_pos + 1) % self.__i_tabu_size

        return selected_value   










