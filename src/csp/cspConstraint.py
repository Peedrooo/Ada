import sys
sys.path.append('../src')

from ifs.model.constraint import Constraint
from cspValue import cspValue

class cspConstraint(Constraint):
    """Implementar todas as restrições/relações das variáveis"""
    def flux_conflict(value, variable_set):
        var = value.variable()
        for v in variable_set:
            if v.get_turma().get_discipline() == var.get_turma().get_discipline() and get_turma().get_num() != var.get_turma().get_num():
                return True
            elif v.get_turma().get_discipline().get_flow() == v.get_turma().get_discipline().get_flow() \
                and (v.get_assigment().get_day() == value.get_day() and v.get_assigment().get_time() == value.get_time()):
                return False
        return True
    # Implementar o get_dia() get_horario na classe cspValeu | na classe class adicionar atributo de id
    # Implementar o get_assigment na classe cspVariable

    # Verificar se vale a pena ter essa restrição, talvez seja melhor remover o valor nos outros domínios quando atribuido
    def resource_conflict(value, variable_set):
        for v in variable_set:
            if v.get_assigment().get_time() == value.get_time() and v.get_assigment().get_day() == value.get_day() \
                and v.get_assigment().get_room() == value.get_room():
                return False
        return True
    
    def lab_conflict(value):
        var = value.variable()
        if not var.get_turma().get_discipline().get_lab():
            return True
        elif not value.get_room().get_isLab() and var.get_turma().get_isPrime():
            return False
        else:
            return True
        
    def room_load_conflict(value):
        if value.variable().get_turma().get_students() > value.get_room().get_supported_load():
            return False
    # Adicionar get_supported_load na classe local

    def same_class_time_conflict(value, variable_set):
        var = value.variable()
        for v in variable_set:
            if var.get_turma().get_num() == v.get_turma().get_num() and v.get_assigment().get_day == value.get_day() \
                and v.get_assigment().get_time == value.get_time():
                return False
        return True
    
# Soft Constraint
    def room_sugested_conflict(value):
            if value.variable().get_turma().get_students() > value.get_room().get_suggested_load():
                return False
        # Adicionar get_supported_load na classe local
    
    def saturday_conflict(value):
        if value.get_day == 7:
            return False
        else:
            return True
    
    def time_conflict(value):
        if value.get_time() == 5 or value.get_time() == 6 or value.get_time() >= 11:
            return False
        else:
            return True
        
    

# End Constraint

    def variables(self):
        """
        Retorna as variáveis associadas a esta restrição.
        Este método precisa ser implementado por subclasses.
        """
        raise NotImplementedError("O método 'variables' precisa ser implementado.")

    def compute_conflicts(self, value, conflicts):
        """
        Calcula os conflitos associados a um valor.
        Este método precisa ser implementado por todas as subclasses.
        """
        raise NotImplementedError("O método 'compute_conflicts' precisa ser implementado.")
        