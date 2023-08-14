# Laila Bahman
# testFile.py for lab07

from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue

def test_Pizza():
    assert Pizza('S').getSize() == 'S'
    assert Pizza('M').getSize() == 'M'
    assert Pizza('L').getSize() == 'L'

def test_CustomPizza():
    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    assert cp1.getPizzaDetails() == \
           'CUSTOM PIZZA\nSize: L\nToppings:\n\t+ extra cheese\n\t+ sausage\nPrice: $14.00\n'
    cp2 = CustomPizza('S')
    cp2.addTopping('pepperoni')
    cp2.addTopping('mushroom')
    # print(cp2.getPizzaDetails())
    # print('CUSTOM PIZZA\nSize: S\nToppings:\n\t+ pepperoni\n\t+ mushroom\nPrice: $9.00\n')
    assert cp2.getPizzaDetails() == \
           'CUSTOM PIZZA\nSize: S\nToppings:\n\t+ pepperoni\n\t+ mushroom\nPrice: $9.00\n'
    cp3 = CustomPizza('S')
    assert cp3.getPizzaDetails() == \
           'CUSTOM PIZZA\nSize: S\nToppings:\nPrice: $8.00\n'

def test_SpecialtyPizza():
    sp1 = SpecialtyPizza('S', 'Carne-more')
    assert sp1.getPizzaDetails() == \
           'SPECIALTY PIZZA\nSize: S\nName: Carne-more\nPrice: $12.00\n'
    sp2 = SpecialtyPizza('M', 'Hawaiian Deluxe')
    assert sp2.getPizzaDetails() == \
           'SPECIALTY PIZZA\nSize: M\nName: Hawaiian Deluxe\nPrice: $14.00\n'

def test_PizzaOrder():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) #12:30:00 PM
    order.addPizza(cp1)
    order.addPizza(sp1)
    # print(order.getOrderDescription())
    # print('******\nOrder Time: 123000\nCUSTOM PIZZA\nSize: S\nToppings:\n\t+ extra cheese\n\t+ sausage\nPrice: $9.00\n\n----\nSPECIALTY PIZZA\nSize: S\nName: Carne-more\nPrice: $12.00\n\n----\nTOTAL ORDER PRICE: $21.00\n******\n')
    assert order.getOrderDescription() == \
           '******\nOrder Time: 123000\nCUSTOM PIZZA\nSize: S\nToppings:\n\t+ extra cheese\n\t+ sausage\nPrice: $9.00\n\n----\nSPECIALTY PIZZA\nSize: S\nName: Carne-more\nPrice: $12.00\n\n----\nTOTAL ORDER PRICE: $21.00\n******\n'
    cp2 = CustomPizza('M')
    cp2.addTopping('pepperoni')
    cp2.addTopping('mushroom')
    cp2.addTopping('olive')
    sp2 = SpecialtyPizza('L', 'Hawaiian Deluxe')
    order = PizzaOrder(113249) #11:32:49 AM
    order.addPizza(cp2)
    order.addPizza(sp2)
    assert order.getOrderDescription() == \
           '******\nOrder Time: 113249\nCUSTOM PIZZA\nSize: M\nToppings:\n\t+ pepperoni\n\t+ mushroom\n\t+ olive\nPrice: $12.25\n\n----\nSPECIALTY PIZZA\nSize: L\nName: Hawaiian Deluxe\nPrice: $16.00\n\n----\nTOTAL ORDER PRICE: $28.25\n******\n'

def test_OrderQueue():
    cp1 = CustomPizza('S')
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000)
    order.addPizza(cp1)
    order.addPizza(sp1)
    q = OrderQueue()
    q.addOrder(order)
    assert q.processNextOrder() == \
           '******\nOrder Time: 123000\nCUSTOM PIZZA\nSize: S\nToppings:\n\t+ extra cheese\n\t+ sausage\nPrice: $9.00\n\n----\nSPECIALTY PIZZA\nSize: S\nName: Carne-more\nPrice: $12.00\n\n----\nTOTAL ORDER PRICE: $21.00\n******\n'
