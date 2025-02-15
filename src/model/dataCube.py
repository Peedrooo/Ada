from collections import defaultdict

class Cube:
    def __init__(self, locals: list, days, horarios):
        self.data = {}
        self.kinds = set()
        self.available_slots = {}
        
        for local in locals:
            self.kinds.add(local['type'])

        for kind in self.kinds:
            self.data[kind] = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))
            self.available_slots[kind] = set()

            for local in [l['name'] for l in locals if l['type'] == kind]:
                for day in days:
                    for horario in horarios:
                        self.data[kind][local][day][horario] = None
                        self.available_slots[kind].add((local, day, horario))

    def set_value(self, kind, local, day, horario, value):
        """Insere um valor em um horário específico."""
        if (kind, local, day, horario) in self.available_slots:
            self.data[kind][local][day][horario] = value
            self.available_slots.remove((kind, local, day, horario))  # Remove o slot do conjunto
        else:
            raise ValueError("Slot já ocupado ou inválido")
        
        
    def get_value(self, kind, local, day, horario):
        return self.data[kind][local][day][horario]
    
    def rum_comum(self, discipline):
        """
        Procura o primeiro horário disponível e preenche com a disciplina.
        Retorna o local, dia e horário preenchidos.
        """
        kind = discipline['type']
        name = discipline['name']
        
        # Itera apenas pelos slots disponíveis
        for slot in self.available_slots:
            slot_kind, local, day, horario = slot
            if slot_kind == kind:  # Verifica se o tipo bate
                self.data[kind][local][day][horario] = name
                self.available_slots.remove(slot)  # Remove o slot preenchido
                return (local, day, horario)
        
        return None  # Nenhum horário disponível para esse tipo

    def reset(self):
        for kind in self.data:
            for local in self.data[kind]:
                for day in self.data[kind][local]:
                    for horario in self.data[kind][local][day]:
                        self.data[kind][local][day][horario] = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "\n".join(
            f"({kind}, {local}, {day}, {horario}): {value}"
            for kind, locals in self.data.items()
            for local, schedule in locals.items()
            for day, horarios in schedule.items()
            for horario, value in horarios.items()
        )

locals = [
    'I10', 'MOCAP', 'I9', 'S10', 'S9', 'I6',
    'I3', 'I7', 'S1', 'S3', 'S2', 'S4', 'S6',
    'S7', 'I5', 'I4', 'ANFITEATRO'
    ]
days = ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB']
horarios = [
    '10:00-11:50', '08:00-09:50', '16:00-17:50',
    '14:00-15:50', '12:00-13:50', '18:00-19:50'
    ]

if __name__ == '__main__':
    cube = Cube(locals, days, horarios)
    print(cube)
