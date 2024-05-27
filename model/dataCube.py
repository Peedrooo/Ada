class Cube:
    def __init__(self, locals, days, horarios):
        self.data = {}
        for local in locals:
            if local not in self.data:
                self.data[local] = {}
            for day in days:
                if day not in self.data[local]:
                    self.data[local][day] = {}
                for horario in horarios:
                    self.data[local][day][horario] = None

    def set_value(self, local, day, horario, value):
        if (
                local in self.data and
                day in self.data[local] and
                horario in self.data[local][day]
                ):
            self.data[local][day][horario] = value
        else:
            raise ValueError("Invalid local, day, or horario")

    def get_value(self, local, day, horario):
        return self.data.get(local, {}).get(day, {}).get(horario, None)

    def reset(self):
        for local in self.data:
            for day in self.data[local]:
                for horario in self.data[local][day]:
                    self.data[local][day][horario] = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        result = []
        for local in self.data:
            for day in self.data[local]:
                for horario in self.data[local][day]:
                    value = self.data[local][day][horario]
                    result.append(f"({local}, {day}, {horario}): {value}")
        return "\n".join(result)


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

cube = Cube(locals, days, horarios)

cube.reset()
