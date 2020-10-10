from ..Creature import *


class Animal(Creature):
    type_count = 0
    def __init__(self):
        super(Animal, self).__init__()
        print("animal created")
        Animal.type_count = Animal.type_count + 1
