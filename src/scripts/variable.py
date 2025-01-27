

class variable():
    def __init__(self, Class):
        self.Class = Class
        self.domain
        self.value
        self.is_assigned = False

    def assign(self, new_value):
        self.value = new_value
        self.is_assigned = True


    def unassign(self):
        self.value = None
        self.is_assigned = False

    def init_domain(self, locals, days, times):
        self.domain = [(local, day, time) for day in days for time in times for local in locals]