import sys
sys.path.append('./src')
from typing import List
from model.classDemand import ClassDemand
from model.maxHeap import MaxHeap


class GenerateClasses:

    def __init__(self, classDemand: List[ClassDemand]):
        self.classDemand = classDemand
        self.classroom_list = []  # Lista de turmas geradas
        self.turma_id = 1  # Inicializa o contador de ID das turmas

    def add_turma(self, disciplina, qnt_interesse):
        tamanhos = [15, 20, 25, 30, 45, 50, 70, 85, 130, 245]

        for tamanho in tamanhos:
            if qnt_interesse <= tamanho:
                turma = ClassDemand(
                    discipline=disciplina, 
                    students=qnt_interesse
                )
                turma.recover_discipline()  
                turma.turma_size = tamanho
                turma.id = self.turma_id 
                # turma.type = self.dis
                self.turma_id += 1  # Incrementa o ID para a próxima turma

                self.classroom_list.append(turma)
                
                qnt_interesse -= tamanho
                break  # Sai do loop após criar a turma

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
            qnt_interesse = self.add_turma(disciplina, qnt_interesse)
            if qnt_interesse > 0:
                HEAP.push((qnt_interesse, disciplina))

    def split_by_workload(self):
        new_classroom_list = []
        for turma in self.classroom_list:
            workload = turma.discipline.workload  # Obtém o workload
            num_fragmentos = max(1, workload // 30)  # Divide em fragmentos de 30
            
            for part in range(1, num_fragmentos + 1):
                nova_turma = ClassDemand(
                    discipline=turma.discipline,
                    students=turma.students
                )
                # nova_turma.recover_discipline()  # Recupera a disciplina original
                nova_turma.turma_size = turma.turma_size  # Mantém o tamanho original
                nova_turma.id = turma.id  # Mantém o mesmo ID
                nova_turma.part = part  # Novo atributo indicando a parte
                nova_turma.type = nova_turma.discipline.type  # Novo atributo indicando o tipo

                new_classroom_list.append(nova_turma)

        self.classroom_list = new_classroom_list  # Atualiza a lista com turmas fragmentadas

    def get_classroom(self):
        HEAP = MaxHeap(self.classDemand)
        self.gera_turmas(HEAP)
        self.split_by_workload()  # Aplica a fragmentação por workload
        return self.classroom_list
