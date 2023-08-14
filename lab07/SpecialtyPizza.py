# Laila Bahman
# SpecialtyPizza.py

from Pizza import Pizza

class SpecialtyPizza(Pizza):

    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
        if (self.size == 'S'):
            self.price = 12.00
        elif (self.size == 'M'):
            self.price = 14.00
        elif (self.size == 'L'):
            self.price = 16.00

    def getPizzaDetails(self):
        size = 'SPECIALTY PIZZA\nSize: ' + str(self.size) + '\n'
        name = 'Name: ' + str(self.name) + '\n'
        price = 'Price: $' + str('{:.2f}'.format(self.price)) + '\n'
        output = size + name + price
        return output
