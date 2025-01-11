from model.dataCube import Cube
from app.database.disciplineStorage import DisciplineStorage
from app.database.teacherStorage import TeacherStorage
from app.database.classromStorage import ClassromStorage

class CSP:
    def __init__(self):
        self.disciplineStorage = DisciplineStorage()
        self.teacherStorage = TeacherStorage()
        self.classromStorage = ClassromStorage()            
    
    def load_data(self, dataPath):
        self.disciplineStorage.load_disciplines(dataPath + '/disciplines.txt')
        self.teacherStorage.load_teachers(dataPath + '/teachers.txt')
        self.classromStorage.load_classroms(dataPath + '/classroms.txt')

    def set_data_cube(self):
        days = ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB']
        horarios = [
            '08:00-09:50', '10:00-11:50', '12:00-13:50' 
            # '14:00-15:50', '16:00-17:50', '18:00-19:50'
            ]

        cube = Cube(
            self.classromStorage.list_classroms(),
            days,
            horarios
            )
        return cube

    def run_csp(self, cube: Cube):
        for discipline in self.disciplineStorage.get_all():
            if discipline.workload > 30:
                pass
            elif discipline.workload > 60:
                pass
            print(discipline.workload)

        pass

    def run(self, dataPath):
        self.load_data(dataPath)
        cube = self.set_data_cube()
        self.run_csp(cube)
        # print(cube)

if __name__ == '__main__':
    csp = CSP()
    csp.run('src/data')
