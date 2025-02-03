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
                # Criando um novo objeto ClassDemand com ID e tamanho da turma
                turma = ClassDemand(
                    discipline=disciplina,  # Mantendo o nome original
                    students=qnt_interesse
                )
                turma.recover_discipline()  # Recupera a disciplina original
                turma.turma_size = tamanho  # Adiciona atributo de tamanho
                turma.id = self.turma_id  # Adiciona um ID único à turma
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

    def get_classroom(self):
        HEAP = MaxHeap(self.classDemand)
        self.gera_turmas(HEAP)
        return self.classroom_list  # Retorna lista de ClassDemand com ID e tamanho da turma
