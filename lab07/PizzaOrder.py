# Laila Bahman
# PizzaOrder.py

from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder(Pizza):
    def __init__(self, time):
        self.pizzas = []
        self.time = time
    def getTime(self):
        return self.time
    def setTime(self, time):
        self.time = time
    def addPizza(self,pizza):
        self.pizzas.append(pizza)
    def getOrderDescription(self):
        price = 0.00
        time = "******\nOrder Time: " + str(self.time) + "\n"
        for x in self.pizzas:
            time += x.getPizzaDetails() + "\n----\n" 
            price += x.getPrice()
        time += "TOTAL ORDER PRICE: $" + str("{:.2f}".format(price)) + "\n******\n"
        return time

