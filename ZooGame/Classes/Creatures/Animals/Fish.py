from .Animal import *


class Fish(Animal):
    type_count = 0
    def __init__(self):
        super(Fish, self).__init__()
        print("created fish")
        Fish.type_count = Fish.type_count + 1