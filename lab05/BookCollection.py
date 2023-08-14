# Laila Bahman

from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:


    
    def __init__(self):
        self.head = None


    def isEmpty(self):
        return self.head == None


    def getNumberOfBooks(self):
        x = self.head
        count = 0
        while x != None:
            count += 1
            x = x.getNext()
        return count


    def insertBook(self, book):
        stop = False
        last = None
        current = self.head

        while current != None and not stop:
            if current.getData() > book:
                stop = True
            else:
                last = current
                current = current.getNext()

        x = BookCollectionNode(book)
        if last == None:
            x.setNext(self.head)
            self.head = x
        else:
            x.setNext(current)
            last.setNext(x)


    def getBooksByAuthor(self, author):
        x = self.head
        output = ""
        while x != None:
            if x.getData().getAuthor().lower() == author.lower():
                output = output + x.getData().getBookDetails() + "\n"
            x = x.getNext()
        return output


    def getAllBooksInCollection(self):
        x = self.head
        output = ""
        while x != None:
            output = output + x.getData().getBookDetails() + "\n"
            x = x.getNext()
        return output


    def removeAuthor(self, author):
        x = self.head
        last = None 
        while x != None:
            if x.getData().author.lower() == author.lower():
                if last:
                    last.setNext(x.getNext())
                else:
                    self.head = x.getNext()
            else:
                last = x 
            x = x.getNext()

            
    def recursiveSearchTitle(self, title, bookNode):
        if not bookNode:
            return False 
        if bookNode.getData().title.lower() == title.lower():
            return True 
        return self.recursiveSearchTitle(title, bookNode.getNext())
