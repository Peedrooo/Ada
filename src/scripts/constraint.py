
class constraint():
    def __init__(self):
        pass

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
            _,local_v,day_v,horario_v,turma_v = v
            if var.id == turma_v.id and day_v == day \
                and horario_v == horario:
                return False
        return True
