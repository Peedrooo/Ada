import sys
sys.path.append('../src')
from value import Value
from variable import Variable

class cspValue(Value):
    def __init__(self, variable, value):
        super().__init__(variable, value)