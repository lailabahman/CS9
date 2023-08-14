# Laila Bahman

from Book import Book

class BookCollectionNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        y = self.data
        return y

    def getNext(self):
        z = self.next
        return z

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext
