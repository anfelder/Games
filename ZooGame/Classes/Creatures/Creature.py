class Creature:

    uid = 0 #unique id
    type_count = 0
    def __init__(self):
        #init pet variables
        self.purchase_cost = 0
        self.sell_cost = 0
        self.name = None
        self.creature_id = Creature.uid
        Creature.uid += 1
        Creature.type_count = Creature.type_count + 1

    def print(self):
        self.print_name()

    def print_info(self):
        self.print_name()
        self.print_purchase_cost()
        self.print_sell_cost()
        self.print_id()
        self.print_type_count()

    def print_purchase_cost(self):
        print(self.purchase_cost)

    def print_sell_cost(self):
        print(self.sell_cost)

    def print_name(self):
        print(self.name)

    def print_id(self):
        print(self.creature_id)

    def print_type_count(self):
        print(self.type_count)