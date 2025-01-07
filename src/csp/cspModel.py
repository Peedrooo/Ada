import sys

sys.path.append('../src')

from scripts.generateClasses import GenerateClasses
from csp.cspVariable import cspVariable


class cspModel():
    classes = GenerateClasses(CLASSROOM, SOLICITATION)
    all_classes = classes.get_classroom()
    variable_set = []
    value_set = []
    
    # Inicializa as variáveis
    for turma in all_classes:
        variable_set.push(cspVariable(turma))
    print(variable_set)

    

    
    