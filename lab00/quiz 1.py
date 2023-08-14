'''
def countNonCharacters(s,c):
    if c not in s:
        countNonCharacters(s,c) == s
    else:
        countNonCharacters(s,c) == s-c

assert countNonCharacters("", "a") == 0
assert countNonCharacters("CMPSC9", "a") == 6
assert countNonCharacters("CMPSC9", "C") == 4
assert countNonCharacters("ZZZ", "Z") == 0
assert countNonCharacters("aAaAa", "A") == 3
'''


class Car:
    
    def setModel(self, model):
        self.model = model
    def setYear(self, year):
        self.year = year
    def getModel(self):
        return model
    def getYear(self):
        return year

c1 = Car("Prius", 2018)
assert c1.getModel() == "Prius"
assert c1.getYear() == 2018
c1.setModel("Accord")
c1.setYear(2015)
assert c1.getModel() == "Accord"
assert c1.getYear() == 2015
