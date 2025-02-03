import sys

sys.path.append('./src')

from model.classDemand import ClassDemand

class variable():
    def __init__(self, Class:ClassDemand, domain):
        self.Class = Class
        self.domain = domain
        self.value = None
        self.is_assigned = False

    def assign(self, new_value):
        self.value = new_value
        self.is_assigned = True

    def unassign(self):
        self.value = None
        self.is_assigned = False