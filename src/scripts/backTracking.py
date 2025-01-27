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
            if var.Class.parte == 1:
                for val in self.csp.available_slots:
                    local, day, _ = val
                    if day == 'SEG' or day == 'TER' or day == 'QUA' and var.Class.students <= local.supported_load:
                        value_order.append(val)
                for val in self.csp.available_slots:
                    local, day, _ = val
                    if var.Class.students <= local.supported_load and day != 'SEG' and day != 'TER' and day != 'QUA':
                        value_order.append(val)
                return self.csp.available_slots # já sabesse que a restrição de sala será quebrada
            
            elif var.Class.parte == 2:
                for assign in assigment:
                    kind, sala_a, day_a, horario_a, turma = assign
                    if turma.id == var.Class.id:
                        if day_a == 'SEG':
                            if (kind, sala_a, 'QUA', horario_a) in self.available_slots:
                                value_order.append(sala_a, 'QUA', horario_a)
                            if (kind, sala_a, 'SEX', horario_a) in self.available_slots:
                                value_order.append(sala_a, 'SEX', horario_a)
                            for val in self.csp.available_slots:
                                _, day, horario = val
                                if day == 'QUA' or day == 'SEX' and horario_a == horario:
                                    value_order.append(val)
                            for val in self.csp.available_slots:
                                _, day, _ = val
                                if day != 'QUA' and day != 'SEX':
                                    value_order.append(val)
                            return value_order
                        elif day_a == 'TER':
                            if (kind, sala_a, 'QUI', horario_a) in self.available_slots:
                                value_order.append(sala_a, 'QUI', horario_a)
                            for val in self.csp.available_slots:
                                _, day, horario = val
                                if day == 'QUI' and horario_a == horario:
                                    value_order.append(val)
                            for val in self.csp.available_slots:
                                _, day, _ = val
                                if day != 'QUI':
                                    value_order.append(val)
                            return value_order
                        elif day_a == 'QUA':
                            if (kind, sala_a, 'SEX', horario_a) in self.available_slots:
                                value_order.append(sala_a, 'SEX', horario_a)
                            for val in self.csp.available_slots:
                                _, day, horario = val
                                if day == 'SEX' and horario_a == horario:
                                    value_order.append(val)
                            for val in self.csp.available_slots:
                                _, day, _ = val
                                if day != 'SEX':
                                    value_order.append(val)
                            return value_order
                #End-for
                return self.csp.available_slots # Não conseguiu fazer nenhuma ordenação aprofundada   
        elif var.Class.workflow == 90:
            if var.Class.parte == 1:
                for val in self.csp.available_slots:
                    local, day, _ = val
                    if day == 'SEG'and var.Class.students <= local.supported_load:
                        value_order.append(val)
                for val in self.csp.available_slots:
                    local, day, _ = val
                    if var.Class.students <= local.supported_load and day != 'SEG':
                        value_order.append(val)
                return self.csp.available_slots # já sabesse que a restrição de sala será quebrada
            elif var.Class.parte == 2:
                for assign in assigment:
                    sala_a, day_a, horario_a, turma_a = assign
                    if turma.id == var.Class.id:
                        if day_a == 'SEG':
                            if (kind, sala_a, 'QUA', horario_a) in self.available_slots:
                                value_order.append(sala_a, 'QUA', horario_a)
                            for val in self.csp.available_slots:
                                _, day, horario = val
                                if day == 'QUA' and horario_a == horario:
                                    value_order.append(val)
                            for val in self.csp.available_slots:
                                _, day, _ = val
                                if day != 'QUA':
                                    value_order.append(val)
                            return value_order
                #End-for
                return self.csp.available_slots # Não conseguiu fazer nenhuma ordenação aprofundada
            elif value.Class.parte == 3:
                for assign in assigment:
                    sala_a, day_a, horario_a, turma_a = assign
                    if turma.id == value.Class.id:
                        if day_a == 'QUA':
                            if (kind, sala_a, 'SEX', horario_a) in self.available_slots:
                                value_order.append(sala_a, 'SEX', horario_a)
                            for val in self.csp.available_slots:
                                _, day, horario = val
                                if day == 'SEX' and horario_a == horario:
                                    value_order.append(val)
                            for val in self.csp.available_slots:
                                _, day, _ = val
                                if day != 'SEX':
                                    value_order.append(val)
                            return value_order
                #End-for
                return self.csp.available_slots # Não conseguiu fazer nenhuma ordenação aprofundada  
        elif var.Class.workflow == 30:
            # Única estratégia que consegui pensar foi evitar slots que sejam potências escolhas para disciplinas de mais horas
            for val in self.csp.available_slots:
                _, room, day, time, turma = val
                if day == 'TER' or day == 'QUI':
                    value_order.inssert(0, val)
                else:
                    value_order.append(val)
        

    def variable_selection(self, assignment):
        # Valores ordenados conforme o fluxo e se faz parte da mesma turma
        if assignment is None:
            return self.csp.domains[0]
        
    def isConsistent(self, var, value, assigment): # verificar restrições
        pass

    def inference(self, var, value):     # Forward checking
        pass

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
    
    

