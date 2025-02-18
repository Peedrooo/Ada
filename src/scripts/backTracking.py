import sys
import random
import time
import traceback
sys.path.append('./src')

from scripts.classCSP import classCSP
from scripts.constraint import constraint
from scripts.variable import variable
from scripts.generateClasses import GenerateClasses
from scripts.interface import Interface
from app.database.classromStorage import classrom_storage
from app.database.classDemandStorage import class_demand_storage
from model.classDemand import ClassDemand
from model.discipline import Discipline
from model.classrom import Classrom
from typing import List

class BackTracking:

    def __init__(self, csp:classCSP):
        self.csp = csp
        # self.cube = cube  # Conjunto com todas as variáveis e seus valores
    
    def search(self, qnd_turma, assigment:List[variable]):
        # Condição de parada
        if self.isComplete(qnd_turma, assigment):
            return assigment
        
        var = self.variable_selection()
        val = self.order_value_selection(var, assigment)

        print(f'Variável: {var.Class.discipline.name} tamanho da turma: {var.Class.turma_size}')
        print(f'Quantidade de turmas alocadas: {len(assigment)}')
        print(f'lista de valores: {len(val)}')
        for value in val:
            if self.isConsistent(var, value, assigment):
                var.assign(value)
                assigment.append(var)
                # Copia dos domínios para restaurar se necessário
                save_domains = {var: list(var.domain) for var in self.csp.variable_list}
                inference_result = self.inference(var, assigment)
                print(f"🔁 inference retornou: {inference_result}")
                if inference_result:
                    result = self.search(qnd_turma, assigment)      
                    if result:
                        return result
                # Restaura o domínio das variáveis
                for restor_var in self.csp.variable_list:
                    restor_var.domain = save_domains[restor_var]
                var.unassign()
                assigment.pop(-1)
        return False

    def order_value_selection(self, var, assigment):
        value_order = []
        value_score = [(v[0], v[1], v[2]) for v in sorted(
            var.domain, key=lambda v: sum(self.count_conflicts(var, v, other_var) for other_var in self.csp.variable_list if not other_var.is_assigned)
        )]
        
        if var.Class.discipline.workload == 60:
            if var.Class.part == 1:
                for val in value_score:
                    local, day, _ = val
                    if day == 'SEG' or day == 'TER' or day == 'QUA' and var.Class.turma_size <= local.capacity:
                        value_order.append(val)
                for val in value_score:
                    local, day, _ = val
                    if var.Class.turma_size <= local.capacity and day != 'SEG' and day != 'TER' and day != 'QUA':
                        value_order.append(val)
                return value_order if value_order else value_score  # Retorna value_order se não estiver vazio, caso contrário, retorna value_score
            elif var.Class.part == 2:
                for assign in assigment:
                    sala_a, day_a, horario_a = assign.value
                    turma = assign.Class
                    if turma.id == var.Class.id:
                        if day_a == 'SEG':
                            if (sala_a, 'QUA', horario_a) in value_score:
                                value_order.append((sala_a, 'QUA', horario_a))
                            if (sala_a, 'SEX', horario_a) in value_score:
                                value_order.append((sala_a, 'SEX', horario_a))
                            for val in value_score:
                                _, day, horario = val
                                if day == 'QUA' or day == 'SEX' and horario_a == horario:
                                    value_order.append(val)
                            for val in value_score:
                                _, day, horario = val
                                if horario_a != horario or (day != 'QUA' and day != 'SEX'):
                                    value_order.append(val)
                            return value_order if value_order else value_score
                        elif day_a == 'TER':
                            if (sala_a, 'QUI', horario_a) in value_score:
                                value_order.append((sala_a, 'QUI', horario_a))
                            for val in value_score:
                                _, day, horario = val
                                if day == 'QUI' and horario_a == horario:
                                    value_order.append(val)
                            for val in value_score:
                                _, day, _ = val
                                if horario_a != horario or day != 'QUI':
                                    value_order.append(val)
                            return value_order if value_order else value_score
                        elif day_a == 'QUA':
                            if (sala_a, 'SEX', horario_a) in value_score:
                                value_order.append((sala_a, 'SEX', horario_a))
                            for val in value_score:
                                _, day, horario = val
                                if day == 'SEX' and horario_a == horario:
                                    value_order.append(val)
                            for val in value_score:
                                _, day, _ = val
                                if horario_a != horario or day != 'SEX':
                                    value_order.append(val)
                            return value_order if value_order else value_score
                #End-for
                return value_score  # Não conseguiu fazer nenhuma ordenação aprofundada   
        elif var.Class.discipline.workload == 90:
            if var.Class.part == 1:
                for val in value_score:
                    local, day, _ = val
                    if day == 'SEG'and var.Class.turma_size <= local.capacity:
                        value_order.append(val)
                for val in value_score:
                    local, day, _ = val
                    if var.Class.turma_size <= local.capacity and day != 'SEG':
                        value_order.append(val)
                return value_order if value_order else value_score  # Retorna value_order se não estiver vazio, caso contrário, retorna value_score
            elif var.Class.part == 2:
                for assign in assigment:
                    sala_a, day_a, horario_a = assign.value
                    turma = assign.Class
                    if turma.id == var.Class.id:
                        if day_a == 'SEG':
                            if (sala_a, 'QUA', horario_a) in value_score:
                                value_order.append((sala_a, 'QUA', horario_a))
                            for val in value_score:
                                _, day, horario = val
                                if day == 'QUA' and horario_a == horario:
                                    value_order.append(val)
                            for val in value_score:
                                _, day, _ = val
                                if horario_a != horario or day != 'QUA':
                                    value_order.append(val)
                            return value_order if value_order else value_score
                #End-for
                return value_score  # Não conseguiu fazer nenhuma ordenação aprofundada
            elif var.Class.part == 3:
                for assign in assigment:
                    sala_a, day_a, horario_a = assign.value
                    turma_a = assign.Class
                    if turma_a.id == var.Class.id:
                        if day_a == 'QUA':
                            if (sala_a, 'SEX', horario_a) in value_score:
                                value_order.append((sala_a, 'SEX', horario_a))
                            for val in value_score:
                                _, day, horario = val
                                if day == 'SEX' and horario_a == horario:
                                    value_order.append(val)
                            for val in value_score:
                                _, day, _ = val
                                if horario_a != horario or day != 'SEX':
                                    value_order.append(val)
                            return value_order if value_order else value_score
                #End-for
                return value_score  # Não conseguiu fazer nenhuma ordenação aprofundada  
        elif var.Class.discipline.workload == 30:
            # Única estratégia que consegui pensar foi evitar slots que sejam potências escolhas para disciplinas de mais horas
            for val in value_score:
                _, day, _ = val
                if day == 'TER' or day == 'QUI':
                    value_order.insert(0, val)
                else:
                    value_order.append(val)
            return value_order if value_order else value_score  # Retorna value_order se não estiver vazio, caso contrário, retorna value_score
        return value_score  # Não conseguiu fazer nenhuma ordenação aprofundada        
    
    def variable_selection(self):
        return min(
        (var for var in self.csp.variable_list if not var.is_assigned),
        key=lambda v: len(v.domain),
        default=None
    )
        # Valores ordenados conforme o fluxo e se faz parte da mesma turma
        # for var in self.csp.variable_list:
        #     # print(var.Class.discipline.name)
        #     if not var.is_assigned:
        #         return var
        
    def isConsistent(self, var, value, assigment): # verificar restrições
        if not self.csp.constraints.verify(var, value, assigment):
            return False
        return True
        
    def inference(self, assigned_variable, assigment):
        try:
            # print("🔍 Entrou na função inference")
            # print("📌 Assignment recebido:", assigment)

            for var in self.csp.variable_list:
                if var != assigned_variable and not var.is_assigned:
                    # print(f"🔎 Processando variável: {var}")

                    var.domain = [value for value in var.domain if self.csp.constraints.verify(var, value, assigment)]     

                    if not var.domain:  # Se o domínio ficou vazio
                        # print(f"❌ Domínio esvaziado para {var}, retornando False.")
                        return False

            # print("✅ inference finalizou normalmente.")
            return True
        except Exception as e:
            print(f"⚠️ Erro inesperado em inference: {e}")
            return False

    def isComplete(self, total_turma, assigment):
        if total_turma == len(assigment) or 552 == len(assigment): # Adicionas atributo assignments no csp
            return True
        else:
            return False
        
    def count_conflicts(self, var, value, other_var):
        count = 0
        var.assign(value)
        for d in other_var.domain:
            if self.csp.constraints.flux_conflict(other_var, d, var):
                count += 1
            if self.csp.constraints.resource_conflict(d, var):
                count += 1
            if self.csp.constraints.same_class_time_conflict(other_var, d, var):
                count += 1
        var.unassign()
        return count
    
def mock_discipline():
    f = open("src/data/disciplines.txt", "r")
    discipline = []
    for line in f:
        name_, flow_, workload_, type_ = line.split("-")
        discipline.append(Discipline(
                name=name_,
                flow=int(flow_),  # Convertendo para inteiro, se necessário
                workload=int(workload_),
                type=type_
            ))
    f.close()
    return discipline

def mock_class(disciplines:list[Discipline]):
    turma = []
    i=0
    random.seed(None)
    for d in disciplines:
        match d.workload:
            case 90:
                for a in range(1, 4):
                    turma.append(ClassDemand(
                        discipline = d,
                        students=0,
                        turma_size = random.randint(30, 200),
                        id = i+1,
                        part = a
                    ))
            case 60:
                for a in range(1, 3):
                    turma.append(ClassDemand(
                        discipline = d,
                        students=0,
                        turma_size = random.randint(30, 200),
                        id = i+1,
                        part = a
                    ))
            case 30:
                turma.append(ClassDemand(
                        discipline = d,
                        students=0,
                        turma_size = random.randint(30, 200),
                        id = i+1,
                        part = 1
                    ))
            case _:
                print("Classe com workload inexistente")
                return None
        i+=1
    return turma

def mock_local():
    f = open("src/data/classroms.txt", "r")
    list_local = []
    for line in f:
        name_, capacity_, type_ = line.split("-")
        list_local.append(Classrom(
                name=name_,
                capacity=int(capacity_),
                type=type_
            ))
    f.close()
    return list_local

if __name__ == "__main__":
    locals = classrom_storage.list_classroms()
    print(f'Quantidade de locais {len(locals)}')
    class_demand = class_demand_storage.return_class_demands()
    cources = GenerateClasses(class_demand)
    days = ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB']
    horarios = [
    '10:00-11:50', '08:00-09:50', '16:00-17:50',
    '14:00-15:50'
    ]

    tempo_inicial = time.time()
    turmas = cources.get_classroom()
    print(f'Quantidade de turmas {len(turmas)}')
    restrincao = constraint()
    csp = classCSP(
        locals = locals,
        days = days,
        times = horarios,
        cources = turmas,
        constraint = restrincao
    )
    csp.init_variables()
    print("Inicialização terminou...")
    csp.sort_variables()
    print("Ordenação das variáveis terminou...")
    back_tracking_search = BackTracking(csp)
    assigment_list = []

    try:
        assigment = back_tracking_search.search(len(turmas), assigment_list)
    except Exception as e:
        print(f"⚠️ Erro detectado em search: {e}")
        traceback.print_exc()

    tempo_final = time.time()
    duracao = tempo_final - tempo_inicial
    if assigment:  # Se search retornou algo diferente de False
        ui = Interface(assigment)
        ui.draw("./grade.txt")
    else:
        print("❌ Nenhuma solução encontrada!")
    
    # Exibir os resultados
    print(f"Tempo inicial: {tempo_inicial:.6f} segundos")
    print(f"Tempo final: {tempo_final:.6f} segundos")
    print(f"Duração da execução: {duracao:.6f} segundos")
    pass
