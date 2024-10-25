class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLangauge(self):
        print("Default language is python")

e1 = Employee("Vedant", 3041)
e1.showDetails()
e2 = Programmer("Aditya", 3058) #Programmer is inherit classs of employee
e2.showDetails() #function from employee can be called through programmer but not vice versa
e2.showLangauge()