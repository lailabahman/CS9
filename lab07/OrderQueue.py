# Laila Bahman
# OrderQueue.py

from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder

class QueueEmptyException(Exception):
    pass
class OrderQueue(Pizza):
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    def percUp(self, piz):
        while piz // 2 > 0:
            if self.heapList[piz].getTime() < self.heapList[piz // 2].getTime():
                tmp = self.heapList[piz // 2]
                self.heapList[piz // 2] = self.heapList[piz]
                self.heapList[piz] = tmp
            piz = piz //2
    def addOrder(self, pizzaOrder):
        self.heapList.append(pizzaOrder)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
    def percDown(self, piz):
        while piz*2 <= self.currentSize:
            mc = self.minChild(piz)
            if self.heapList[piz].getTime() > self.heapList[mc].getTime():
                tmp = self.heapList[piz]
                self.heapList[piz] = self.heapList[mc]
                self.heapList[mc] = tmp
            piz = mc
    def minChild(self, piz):
        if piz*2+1 > self.currentSize:
            return piz*2
        else:
            if self.heapList[piz*2].getTime() < self.heapList[piz*2+1].getTime():
                return piz*2
            else:
                return piz * 2 + 1
    def processNextOrder(self):
        if (self.currentSize == 0):
            raise QueueEmptyException()
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval.getOrderDescription()
        
