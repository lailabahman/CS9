# Lab00, CS 9, Laila Bahman
'''
a = int(input('pick a number between 1 and 4: '))

list1 = []
list2 = []

i = random.randint(0,4)
for e in range(len(i)):
    import random
    n = random.randint(1,4)
    list1.append(n)

j = random.randint(1,4)
for e in range(len(j)):
    import random
    n = random.randint(1,4)
    list2.append(n)

print(list1, list2)
'''

def areElementsInList(list1, list2):
    ''' This function takes two lists as its parameters (list1 and
        list2). Return True if each element in list1 exists in list2.
        Return False otherwise. If list1 contains no elements, True is
        returned.
    '''
    # COMPLETE FUNCTION DEFINITION HERE
    if(len(list1) == 0):
        return True
    for num in range(len(list1)):
        if list1[num] in list2:
            x = True
        else:
            x = False
    return x


assert areElementsInList(["one",2], [0,"one",2,"three"]) == True
assert areElementsInList([],[1,2,3,4]) == True
assert areElementsInList([1,2,3],[1,2]) == False
assert areElementsInList([1,2,3],[3,2,1]) == True


################################################################################


def alternateCase(s):
    ''' This function takes a string parameter (s) and returns a new
        string that flips the case of each alpha character in s.
    '''
    # COMPLETE FUNCTION DEFINITION HERE

    if(len(s) == 0):
        return s
    for p in range(len(s)):
        swap = s.swapcase()
    return swap

assert alternateCase("") == ""
assert alternateCase("This is a Sentence") == "tHIS IS A sENTENCE"
assert alternateCase("CS9") == "cs9"
assert alternateCase("9.95") == "9.95"


################################################################################


def getCharacterCount(s):
    ''' This function takes a string parameter (s) and returns a dictionary
        type where each key in the dictionary is a unique upper-case character
        in s and its associated value is the number of occurences the unique
        character exists in s. Note that the unique characters should be case
        insensitive ("a" and "A" are considered the same and should be stored as
        "A" in the dictionary). Non alpha characters (including whitespaces)
        and their occurences should also be stored in the dictionary.
    '''
    # COMPLETE FUNCTION DEFINITION HERE
    s = s.upper()
    A = {}
    for num in s:
        if num in A:
            A[num] = A[num] + 1
        else:
            A[num] = 1
    return A
    

x = getCharacterCount("This is a Sentence")
assert x.get("S") == 3
assert x.get("P") == None
assert x.get("I") == 2
assert x.get(" ") == 3

y = getCharacterCount("Pi is Approximately 3.14159")
assert y.get("1") == 2
assert y.get("A") == 2
assert y.get("P") == 3
assert y.get(".") == 1
assert y.get(4) == None

