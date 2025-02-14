import sys
sys.path.append('./src')
from typing import List
from model.classDemand import ClassDemand
from model.maxHeap import MaxHeap
from app.database.disciplineStorage import discipline_storage


class GenerateClasses:

    def __init__(self, classDemand: List[ClassDemand]):
        self.classDemand = classDemand
        self.classroom_list = []
        self.turma_id = 1


    def add_turma(self, disciplina, qnt_interesse):
        disciplina_encontrada = discipline_storage.get_discipline(disciplina)
        if disciplina_encontrada.type == 'comum':
            tamanhos = [45, 48, 50, 70, 90, 130]
        else:
            tamanhos = [45, 60, 70]

        for tamanho in tamanhos:

            if qnt_interesse <= tamanho:
                turma = ClassDemand(
                    discipline=disciplina_encontrada, 
                    students=qnt_interesse
                )
                turma.turma_size = tamanho
                turma.id = self.turma_id 
                self.turma_id += 1

                self.classroom_list.append(turma)
                
                qnt_interesse -= tamanho
            elif qnt_interesse >= 130 and  disciplina_encontrada.type == 'comum':
                tamanho = 130
                turma = ClassDemand(
                    discipline=disciplina_encontrada, 
                    students=tamanho
                )
                turma.turma_size = tamanho
                turma.id = self.turma_id
                self.turma_id += 1

                self.classroom_list.append(turma)

                qnt_interesse -= tamanho
            elif qnt_interesse >= 70 and disciplina_encontrada.type != 'comum':
                tamanho = 70
                turma = ClassDemand(
                    discipline=disciplina_encontrada, 
                    students=tamanho
                )
                turma.turma_size = tamanho
                turma.id = self.turma_id
                self.turma_id += 1

                self.classroom_list.append(turma)

                qnt_interesse -= tamanho
        return qnt_interesse

    def gera_turmas(self, HEAP: MaxHeap):
        all_elements = HEAP.all()
        HEAP.clean()

        for qnt_interesse, disciplina in all_elements:
            qnt_interesse = self.add_turma(disciplina.discipline.name, qnt_interesse)
            if qnt_interesse > 0:
                HEAP.push((qnt_interesse, disciplina))

        while len(HEAP):
            qnt_interesse, disciplina = HEAP.pop()
            qnt_interesse = self.add_turma(disciplina.discipline.name, qnt_interesse)
            if qnt_interesse > 0:
                HEAP.push((qnt_interesse, disciplina))

    def split_by_workload(self):
        new_classroom_list = []
        for turma in self.classroom_list:
            workload = turma.discipline.workload  
            num_fragmentos = max(1, workload // 30)
            
            for part in range(1, num_fragmentos + 1):
                nova_turma = ClassDemand(
                    discipline=turma.discipline,
                    students=turma.students
                )
                nova_turma.turma_size = turma.turma_size
                nova_turma.id = turma.id
                nova_turma.part = part
                nova_turma.type = nova_turma.discipline.type

                new_classroom_list.append(nova_turma)

        self.classroom_list = new_classroom_list  # Atualiza a lista com turmas fragmentadas

    def get_classroom(self):
        print('Generating classes...')
        HEAP = MaxHeap(self.classDemand)
        print('Heap created')
        self.gera_turmas(HEAP)
        print('Classes generated')
        self.split_by_workload()
        print('Classes splitted')
        return self.classroom_list
    
