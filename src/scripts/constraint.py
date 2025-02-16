
class constraint():
    def flux_conflict(self, var, value, v):
        # Restrição não se aplica para disciplina optativa 
        if var.Class.discipline.flow == 0:
            return False
        
        _, day, horario = value
        _, day_v, horario_v = v.value
        turma = v.Class
        if turma.discipline == var.Class.discipline and turma.id != var.Class.id:
            return False
        elif turma.discipline.flow == var.Class.discipline.flow \
            and (day_v == day and horario_v == horario):
            if turma.discipline.flow <= 3:
                return True
            elif var.Class.discipline.course == turma.discipline.course:
                return True
        return False

    
    def resource_conflict(self, value, v):
        local, day, horario = value
        local_a, day_a, horario_a = v.value
        if horario_a == horario and day_a == day \
            and local_a == local:
            return True
        return False
    
    def same_class_time_conflict(self, var, value, v):
        _, day, horario = value
        _,day_v,horario_v = v.value
        turma_v = v.Class
        if var.Class.id == turma_v.id \
            and day_v == day and horario_v == horario:
            return True
        return False
    
    def lab_conflict(self, var, value):
        local,_,_ = value
        # print(f'Tipo Disciplina: {var.Class.discipline.type}')
        # print(f'Tipo sala: {local.type}')
        if var.Class.discipline.type == 'comum':
            return False
        elif local.type != var.Class.discipline.type:
            return True
        else:
            return False

    def room_load_conflict(self, var, value):
        local,_,_ = value
        if var.Class.turma_size > local.capacity:
            return True
        return False
    
    def verify(self, var, value, assigment):
        if self.lab_conflict(var, value):
            # print('erro lab')
            return False
        if self.room_load_conflict(var, value):
            # print('erro room_load')
            return False
        for v in assigment:
            if v != var and v != []:
                if self.resource_conflict(value, v):
                    # print('erro resource')
                    return False
                if self.flux_conflict(var, value, v):
                    # print('erro flux')
                    return False
                if self.same_class_time_conflict(var, value, v):
                    # print('erro same class')
                    return False
        return True
