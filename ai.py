
from random import randint

class AI:
    def turn(self,map):
        print map
        return randint(0, 9),randint(0, 9)
