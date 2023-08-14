# Laila Bahman

from Book import Book
from BookCollection import BookCollection
from BookCollectionNode import BookCollectionNode


b0 = Book("Cujo", "King, Stephen", 1981)
b1 = Book("The Shining", "King, Stephen", 1977)
b2 = Book("Ready Player One", "Cline, Ernest", 2011)
b3 = Book("Rage", "King, Stephen", 1977)



def test_Book():
    assert b0.getTitle() == "Cujo"
    assert b1.getAuthor() == "King, Stephen"
    assert b2.getYear() == 2011
    assert b3.getBookDetails() == "Title: Rage, Author: King, Stephen, Year: 1977"


def test_addingNodes():
    assert BookCollectionNode(b0).getData() == b0
    assert BookCollectionNode(b0).getNext() == None


def test_isEmpty():
    assert BookCollection().isEmpty() == True
