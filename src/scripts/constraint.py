
class constraint():
    def flux_conflict(self, var, value, assigment):
        _, day, horario = value
        for v in assigment:
            _, day_v, horario_v = v.value
            turma = v.Class
            if turma.discipline == var.discipline and turma.id != var.id:
                return True
            elif turma.discipline.flow == var.discipline.flow \
                and (day_v == day and horario_v == horario):
                return False
        return True
    
    def resource_conflict(self, value, assigment):
        local, day, horario = value
        for v in assigment:
            local_a, day_a, horario_a = v.value
            if horario_a == horario and day_a == day \
                and local_a == local:
                return False
        return True
    
    def lab_conflict(self, var, value):
        local,_._ = value
        if var.Class.discipline.type == 'comum':
            return True
        elif not local.type == var.discipline.type :
            return False
        else:
            return True

    def room_load_conflict(self, var, value):
        local,_,_ = value
        if var.Class.turma_size > local.capacity:
            return False
        return True
    
    def same_class_time_conflict(self, var, value, assigment):
        _, day, horario = value
        for v in assigment:
            _,day_v,horario_v = v.value
            turma_v = v.Class
            if var.Class.id == turma_v.id \
                and day_v == day and horario_v == horario:
                return False
        return True
    
    def verify(self, var, value, assigment):
        if self.flux_conflict(var, value, assigment) and \
            self.resource_conflict(value, assigment) and \
            self.lab_conflict(var, value) and \
            self.room_load_conflict(var, value) and \
            self.same_class_time_conflict(var, value, assigment):
            return True
        else:
            return False
