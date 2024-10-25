class Person:
    name = "vedant"
    occ = "Student"

    def info(self):
        print(f"{self.name} is a {self.occ}")

#a = Person()
#a.name = "Divya" #arguments which will store in name and occ respectively
#a.occ = "HR"
#a.info()

class Person:
    def __init__(self,name,occ):
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Vedant", "Student") # a passes as self argumnent and name and occ respectively
b = Person("Adi", "Gamer") # b passes as self

a.info()
b.info()

#construxtor is called automatically when an object is created