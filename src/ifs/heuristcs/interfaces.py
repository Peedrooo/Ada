from abc import ABC, abstractmethod

class VariableSelection:
    @abstractmethod
    def select_Variable(self, solution):
        pass

class ValueSelection:
    @abstractmethod
    def select_Value(self, solution, variable):
        pass

class SolutionComparator:
    @abstractmethod
    def is_Better_Than_Best_Solution(self, current_solution):
        pass
    
class TerminatorCondition:
    @abstractmethod
    def can_Continue(self, current_solution):
        pass
    
