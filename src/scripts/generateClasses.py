import sys

sys.path.append('./src')

from model.classDemand import ClassDemand


class GenerateClasses:

    def __init__(
            self, classDemand: list[ClassDemand]
            ):
        self.CLASSROOM = {}
        self.gera_turmas(classDemand)

    def add_turma(self, e, disciplina, qnt_interesse):
        if qnt_interesse <= 15:
            self.CLASSROOM[15][disciplina['type']].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 15
        elif qnt_interesse <= 25:
            self.CLASSROOM[20][disciplina['type']].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 20
        elif qnt_interesse <= 30:
            self.CLASSROOM[25][disciplina['type']].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 25
        elif qnt_interesse <= 45:
            self.CLASSROOM[30][disciplina['type']].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 30
        elif qnt_interesse <= 50:
            self.CLASSROOM[45][disciplina['type']].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 45
        elif qnt_interesse <= 70:
            self.CLASSROOM[50][disciplina['type']].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 50
        elif qnt_interesse <= 85:
            self.CLASSROOM[70][disciplina['type']].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 70
        elif qnt_interesse <= 130:
            self.CLASSROOM[85][disciplina['type']].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 85
        elif qnt_interesse <= 245:
            self.CLASSROOM[130][disciplina['type']].append(
                (f'Turma_{e}', disciplina, qnt_interesse))
            qnt_interesse -= 130
        else:
            self.CLASSROOM[245][disciplina['type']].append(
                (f'Turma_{e}', disciplina, 245))
            qnt_interesse -= 245
        return qnt_interesse

    def gera_turmas(self, classDemand: list[ClassDemand]):
        e = 0
        for disciplina, qnt_interesse in classDemand:
            e += 1
            qnt_interesse = self.add_turma(e, disciplina, qnt_interesse)

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
    # print(generateClasses.get_classroom())
