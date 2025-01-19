from csp import CSP

class BackTracking:

    def __init__(self, csp, cube):
        self.csp = csp
        self.cube = cube  # Conjunto com todas as variáveis e seus valores
    
    def search(self, csp, assigment, qnd_turma):

        # Condição de parada
        if isComplete(assigment, qnd_turma):
            return assigment
        
        val = order_value_selection(assigment, self.csp)
        var = variable_selection(val, assigment, self.csp)

        for value in val:
            if isConsistent(var, value, assigment):
                assigment.append((var, value))  # Add ao cubo de dado
                inference_result = inference(self.csp, var, value)

                result = search(csp, assigment, qnd_turma)      
                if result is not failure:
                    return result
        return failure

        
    def order_value_selection(self, value, assigment): # Grande impacto na performance
        """ Garantir que a escolha de valores que preservem mais opções para as turmas 
        restantes, reduzindo a probabilidade de atingir um beco sem saída."""
        variable_order = set()
        if value.workflow == 60:
            if value.parte == 1:
                for var in self.csp.available_slots:
                    local, day, _ = var
                    if day == 'SEG' or day == 'TER' or day == 'QUA' and value.students <= local.supported_load:
                        variable_order.append(var)
                for var in self.csp.available_slots:
                    local, day, _ = var
                    if value.students <= local.supported_load and day != 'SEG' and day != 'TER' and day != 'QUA':
                        variable_order.append(var)
                return self.csp.available_slots # já sabesse que a restrição de sala será quebrada
            
            elif value.parte == 2:
                for assign in assigment:
                    sala_a, day_a, horario_a, turma_a = assign
                    if turma.id == value.id:
                        if day_a == 'SEG':
                            if (kind, sala_a, 'QUA', horario_a) in self.available_slots:
                                variable_order.append(sala_a, 'QUA', horario_a)
                            if (kind, sala_a, 'SEX', horario_a) in self.available_slots:
                                variable_order.append(sala_a, 'SEX', horario_a)
                            for var in self.csp.available_slots:
                                _, day, horario = var
                                if day == 'QUA' or day == 'SEX' and horario_a == horario:
                                    variable_order.append(var)
                            for var in self.csp.available_slots:
                                _, day, _ = var
                                if day != 'QUA' and day != 'SEX':
                                    variable_order.append(var)
                            return variable_order
                        elif day_a == 'TER':
                            if (kind, sala_a, 'QUI', horario_a) in self.available_slots:
                                variable_order.append(sala_a, 'QUI', horario_a)
                            for var in self.csp.available_slots:
                                _, day, horario = var
                                if day == 'QUI' and horario_a == horario:
                                    variable_order.append(var)
                            for var in self.csp.available_slots:
                                _, day, _ = var
                                if day != 'QUI':
                                    variable_order.append(var)
                            return variable_order
                        elif day_a == 'QUA':
                            if (kind, sala_a, 'SEX', horario_a) in self.available_slots:
                                variable_order.append(sala_a, 'SEX', horario_a)
                            for var in self.csp.available_slots:
                                _, day, horario = var
                                if day == 'SEX' and horario_a == horario:
                                    variable_order.append(var)
                            for var in self.csp.available_slots:
                                _, day, _ = var
                                if day != 'SEX':
                                    variable_order.append(var)
                            return variable_order
                #End-for
                return self.csp.available_slots # Não conseguiu fazer nenhuma ordenação aprofundada   
        elif value.workflow == 90:
            if value.parte == 1:
                for var in self.csp.available_slots:
                    local, day, _ = var
                    if day == 'SEG'and value.students <= local.supported_load:
                        variable_order.append(var)
                for var in self.csp.available_slots:
                    local, day, _ = var
                    if value.students <= local.supported_load and day != 'SEG':
                        variable_order.append(var)
                return self.csp.available_slots # já sabesse que a restrição de sala será quebrada
            elif value.parte == 2:
                for assign in assigment:
                    sala_a, day_a, horario_a, turma_a = assign
                    if turma.id == value.id:
                        if day_a == 'SEG':
                            if (kind, sala_a, 'QUA', horario_a) in self.available_slots:
                                variable_order.append(sala_a, 'QUA', horario_a)
                            for var in self.csp.available_slots:
                                _, day, horario = var
                                if day == 'QUA' and horario_a == horario:
                                    variable_order.append(var)
                            for var in self.csp.available_slots:
                                _, day, _ = var
                                if day != 'QUA':
                                    variable_order.append(var)
                            return variable_order
                #End-for
                return self.csp.available_slots # Não conseguiu fazer nenhuma ordenação aprofundada
            elif value.parte == 3:
                for assign in assigment:
                    sala_a, day_a, horario_a, turma_a = assign
                    if turma.id == value.id:
                        if day_a == 'QUA':
                            if (kind, sala_a, 'SEX', horario_a) in self.available_slots:
                                variable_order.append(sala_a, 'SEX', horario_a)
                            for var in self.csp.available_slots:
                                _, day, horario = var
                                if day == 'SEX' and horario_a == horario:
                                    variable_order.append(var)
                            for var in self.csp.available_slots:
                                _, day, _ = var
                                if day != 'SEX':
                                    variable_order.append(var)
                            return variable_order
                #End-for
                return self.csp.available_slots # Não conseguiu fazer nenhuma ordenação aprofundada  
        elif value.workflow == 30:
            # Única estratégia que consegui pensar foi evitar slots que sejam potências escolhas para disciplinas de mais horas
            pass
                        
        

    def variable_selection(self, assignment):
        # Valores ordenados conforme o fluxo e se faz parte da mesma turma
        if assignment is None:
            return self.csp.domains[0]
        
    
    def isConsistent(self, var, value): # verificar restrições
        pass

    def inference(self, csp, var, value):     # Forward checking
        pass

    def isComplete(self, total_turma):
        if total_turma == self.cube.assigments: # Adicionas atributo assignments no cubo de dados
            return True
        else:
            return False
        
    def flux_conflict(self, var, value, assigment):
        _, day, horario = value
        for v in assigment:
            _, day_v, horario_v, turma = v
            if turma.discipline == var.discipline and turma.id != var.id:
                return True
            elif turma.discipline.flow == var.discipline.flow \
                and (day_v == day and horario_v == horario):
                return False
        return True
    
    # Verificar se vale a pena ter essa restrição, talvez seja melhor remover o valor nos outros domínios quando atribuido
    def resource_conflict(value, assigment):
        local, day, horario = value
        for v in assigment:
            local_a, day_a, horario_a,_ = v
            if horario_a == horario and day_a == day \
                and local_a == local:
                return False
        return True
    
    def lab_conflict(var, value):
        _,local,_,_ = value
        if var.discipline.type == 'comum':
            return True
        elif not local.lab and var.discipline.type != 'comum': # Adicionar lógica do atributo lab na classe local
            return False
        else:
            return True

    def room_load_conflict(var, value):
        _,local,_,_ = value
        if var.students > local.get_supported_load():
            return False
        return True
    
    def same_class_time_conflict(var, value, assigment):
        var = value.variable()
        _,local,day,horario = value
        for v in assigment:
            _,local_v,dar_v,horario_v,turma_v = v
            if var.id == turma_v.id and day_v == day \
                and horario_v == horario:
                return False
        return True

    

