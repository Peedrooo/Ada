from csp import CSP
from constraint import constraint
from variable   import variable

class BackTracking:

    def __init__(self, csp, cube):
        self.csp = csp
        self.cube = cube  # Conjunto com todas as variáveis e seus valores
    
    def search(self, csp, assigment, qnd_turma):

        # Condição de parada
        if isComplete(assigment, qnd_turma):
            return assigment
        
        var = variable_selection(assigment)
        val = order_value_selection(var, assigment)

        for value in val:
            if isConsistent(var, value, assigment):
                assigment.append((var, value))  # Add ao cubo de dado
                inference_result = inference(self.csp, var, value)

                result = search(csp, assigment, qnd_turma)      
                if result is not failure:
                    return result
        return failure

        
    def order_value_selection(self, var, assigment): # Grande impacto na performance
        """ Garantir que a escolha de valores que preservem mais opções para as turmas 
        restantes, reduzindo a probabilidade de atingir um beco sem saída."""
        value_order = []
        value_score = []
        for v in var.domain:
            conflicts = 0
            for other_var in assigment:
                if not other_var.is_assigned:
                    conflicts = count_conflicts(var, v, other_var, self.csp.constraint)
            value_score.append((v, conflicts))
        value_score.sort(key=lambda x: x[1])

        if var.Class.workflow == 60:
            if var.Class.part == 1:
                for val in var.domain:
                    local, day, _ = val
                    if day == 'SEG' or day == 'TER' or day == 'QUA' and var.Class.students <= local.supported_load:
                        value_order.append(val)
                for val in var.domain:
                    local, day, _ = val
                    if var.Class.students <= local.supported_load and day != 'SEG' and day != 'TER' and day != 'QUA':
                        value_order.append(val)
                return value_order # já sabesse que a restrição de sala será quebrada
            elif var.Class.part == 2:
                for assign in assigment:
                    sala_a, day_a, horario_a = assign.domain
                    turma = assign.Class
                    if turma.id == var.Class.id:
                        if day_a == 'SEG':
                            if (sala_a, 'QUA', horario_a) in value_score:
                                value_order.append(sala_a, 'QUA', horario_a)
                            if (sala_a, 'SEX', horario_a) in value_score:
                                value_order.append(sala_a, 'SEX', horario_a)
                            for val in value_score:
                                _, day, horario = val
                                if day == 'QUA' or day == 'SEX' and horario_a == horario:
                                    value_order.append(val)
                            for val in value_score:
                                _, day, horario = val
                                if horario_a != horario or (day != 'QUA' and day != 'SEX'):
                                    value_order.append(val)
                            return value_order
                        elif day_a == 'TER':
                            if (sala_a, 'QUI', horario_a) in value_score:
                                value_order.append(sala_a, 'QUI', horario_a)
                            for val in value_score:
                                _, day, horario = val
                                if day == 'QUI' and horario_a == horario:
                                    value_order.append(val)
                            for val in value_score:
                                _, day, _ = val
                                if horario_a != horario or day != 'QUI':
                                    value_order.append(val)
                            return value_order
                        elif day_a == 'QUA':
                            if (sala_a, 'SEX', horario_a) in value_score:
                                value_order.append(sala_a, 'SEX', horario_a)
                            for val in value_score:
                                _, day, horario = val
                                if day == 'SEX' and horario_a == horario:
                                    value_order.append(val)
                            for val in value_score:
                                _, day, _ = val
                                if horario_a != horario or day != 'SEX':
                                    value_order.append(val)
                            return value_order
                #End-for
                return value_score # Não conseguiu fazer nenhuma ordenação aprofundada   
        elif var.Class.workflow == 90:
            if var.Class.part == 1:
                for val in value_score:
                    local, day, _ = val
                    if day == 'SEG'and var.Class.students <= local.supported_load:
                        value_order.append(val)
                for val in value_score:
                    local, day, _ = val
                    if var.Class.students <= local.supported_load and day != 'SEG':
                        value_order.append(val)
                return value_order # já sabesse que a restrição de sala será quebrada
            elif var.Class.part == 2:
                for assign in assigment:
                    sala_a, day_a, horario_a = assign
                    turma = assign.Class
                    if turma.id == var.Class.id:
                        if day_a == 'SEG':
                            if (sala_a, 'QUA', horario_a) in value_score:
                                value_order.append(sala_a, 'QUA', horario_a)
                            for val in value_score:
                                _, day, horario = val
                                if day == 'QUA' and horario_a == horario:
                                    value_order.append(val)
                            for val in value_score:
                                _, day, _ = val
                                if horario_a != horario or day != 'QUA':
                                    value_order.append(val)
                            return value_order
                #End-for
                return value_score # Não conseguiu fazer nenhuma ordenação aprofundada
            elif var.Class.part == 3:
                for assign in assigment:
                    sala_a, day_a, horario_a = assign.value
                    turma_a = assign.Class
                    if turma_a.id == var.Class.id:
                        if day_a == 'QUA':
                            if (sala_a, 'SEX', horario_a) in value_score:
                                value_order.append(sala_a, 'SEX', horario_a)
                            for val in value_score:
                                _, day, horario = val
                                if day == 'SEX' and horario_a == horario:
                                    value_order.append(val)
                            for val in value_score:
                                _, day, _ = val
                                if horario_a != horario or day != 'SEX':
                                    value_order.append(val)
                            return value_order
                #End-for
                return value_score # Não conseguiu fazer nenhuma ordenação aprofundada  
        elif var.Class.workflow == 30:
            # Única estratégia que consegui pensar foi evitar slots que sejam potências escolhas para disciplinas de mais horas
            for val in value_score:
                _, day, _ = val
                if day == 'TER' or day == 'QUI':
                    value_order.insert(0, val)
                else:
                    value_order.append(val)
            return value_order
        

    def variable_selection(self, assignment):
        # Valores ordenados conforme o fluxo e se faz parte da mesma turma
        if assignment is None:
            return self.csp.domains[0]
        
    def isConsistent(self, var, value, assigment): # verificar restrições
        for constraint in self.csp.constraints[var]:
            if not constraint.is_satisfied(value, assigment):
                return False
        return True
        
    def inference(self, assigned_variable, assigned_value, constraints):     
        # Copia dos domínios para restaurar se necessário
        reduced_domains = {var: list(var.domains) for var in self.csp.variable_list}

        for var in self.csp.variable_list:
            if var != assigned_variable and not var.is_assigned:  
                # Remove slots inválidos do domínio da variável não atribuída
                for value in var.domains[:]:  
                    if not constraints(assigned_variable, assigned_value, var, value):  
                        reduced_domains[var].remove(value)  

                # Se o domínio ficar vazio, falha na inferência (backtrack necessário)
                if not reduced_domains[var]:
                    return False, None
        return True, reduced_domains

    def isComplete(self, total_turma, assigment):
        if total_turma == len(assigment): # Adicionas atributo assignments no csp
            return True
        else:
            return False
        
    def count_conflicts(var, value, other_var, constraint_obc):
        count = 0
        var.assign(value)
        for d in other_var.domain:
            if not constraint_obc.flux_conflict(other_var, d, [var]):
                count += 1
            if not constraint_obc.resource_conflict(d, [var]):
                count += 1
            if not constraint_obc.same_class_time_conflict(other_var, d, [var]):
                count += 1
        var.unassign()
        return count
    
    

