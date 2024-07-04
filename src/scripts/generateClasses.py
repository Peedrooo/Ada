import sys
import pandas as pd
from random import randint

sys.path.insert(0, './src')

from model.maxHeap import MaxHeap
from data.resources import CLASSROOM


# Read the data
df = pd.read_excel('./src/data/grade_fga.xlsx')

# Get the disciplines
df = df[df['CURSO RESPONSAVEL'] == 'Software'].reset_index(drop=True)
CLASS = df['DISCIPLINA'].unique()

# Generate fake solicitation


def gera_solicitacao(CLASS):
    SOLICITATION = []
    for disciplina in CLASS:
        qnt_interesse, disciplina = randint(10, 900), disciplina
        SOLICITATION.append((qnt_interesse, disciplina))
    return SOLICITATION


SOLICITATION = gera_solicitacao(CLASS)


class GenerateClasses:

    def __init__(
            self, CLASSROOM: dict,
            SOLICITATION: list
            ):
        HEAP = MaxHeap(SOLICITATION)
        self.CLASSROOM = CLASSROOM
        self.gera_turmas(HEAP)

    def add_turma(self, e, disciplina, qnt_interesse):
        if qnt_interesse <= 15:
            self.CLASSROOM[15]['Comon'].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 15
        elif qnt_interesse <= 25:
            self.CLASSROOM[20]['Comon'].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 20
        elif qnt_interesse <= 30:
            self.CLASSROOM[25]['Comon'].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 25
        elif qnt_interesse <= 45:
            self.CLASSROOM[30]['Comon'].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 30
        elif qnt_interesse <= 50:
            self.CLASSROOM[45]['Comon'].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 45
        elif qnt_interesse <= 70:
            self.CLASSROOM[50]['Comon'].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 50
        elif qnt_interesse <= 85:
            self.CLASSROOM[70]['Comon'].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 70
        elif qnt_interesse <= 130:
            self.CLASSROOM[85]['Comon'].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 85
        elif qnt_interesse <= 245:
            self.CLASSROOM[130]['Comon'].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 130
        else:
            self.CLASSROOM[245]['Comon'].append(
                (f'Turma_{e}', disciplina, 245))
            qnt_interesse -= 245
        return qnt_interesse

    def gera_turmas(self, HEAP: MaxHeap):
        e = 0
        all_elements = HEAP.all()
        HEAP.clean()
        for qnt_interesse, disciplina in all_elements:
            e += 1
            qnt_interesse = self.add_turma(e, disciplina, qnt_interesse)
            if qnt_interesse > 0:
                HEAP.push((qnt_interesse, disciplina))

        while len(HEAP):
            qnt_interesse, disciplina = HEAP.pop()
            e += 1
            qnt_interesse = self.add_turma(e, disciplina, qnt_interesse)
            if qnt_interesse > 0:
                HEAP.push((qnt_interesse, disciplina))
        return self.CLASSROOM

    def get_classroom(self):
        return self.CLASSROOM


if __name__ == '__main__':

    generateClasses = GenerateClasses(CLASSROOM, SOLICITATION)
    print(generateClasses.get_classroom())
