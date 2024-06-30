from collections import deque


class CSP:
    def __init__(self, variables, domains, neighbors, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints

def csp_create(locals, days, horarios, disciplinas):
    variables = [(local, day, horario) for local in locals for day in days for horario in horarios]
    domains = {var: disciplinas[:] for var in variables}
    neighbors = {var: [] for var in variables}

    for var in variables:
        local, day, horario = var
        for other in variables:
            if other != var:
                o_local, o_day, o_horario = other
                # Mesmos horários em locais diferentes
                if day == o_day and horario == o_horario:
                    neighbors[var].append(other)
                # Mesmos locais em horários diferentes
                if local == o_local and horario != o_horario:
                    neighbors[var].append(other)
    
    constraints = lambda A, a, B, b: a != b  # As disciplinas devem ser diferentes para não haver conflito

    return CSP(variables, domains, neighbors, constraints)

def ac3(csp):
    queue = deque([(xi, xj) for xi in csp.variables for xj in csp.neighbors[xi]])
    
    while queue:
        (xi, xj) = queue.popleft()
        if revise(csp, xi, xj):
            if not csp.domains[xi]:
                return False  # Domínio de xi ficou vazio
            for xk in csp.neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True

def revise(csp, xi, xj):
    revised = False
    for x in csp.domains[xi][:]:
        if all(not csp.constraints(xi, x, xj, y) for y in csp.domains[xj]):
            csp.domains[xi].remove(x)
            revised = True
    return revised

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

disciplinas = [
    'Matemática', 'Física', 'Química', 'Biologia',
    'História', 'Geografia', 'Inglês', 'Português'
]

csp = csp_create(locals, days, horarios, disciplinas)
ac3_result = ac3(csp)

if ac3_result:
    print("AC-3 conseguiu reduzir os domínios.")
    for var in csp.variables:
        print(f"{var}: {csp.domains[var]}")
else:
    print("AC-3 falhou, um domínio ficou vazio.")
