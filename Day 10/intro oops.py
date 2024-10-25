#CLASSES AND OBJECTS
class Details:
    name = "Vedant"
    occupation = "Student"
    age = 19

    def info(self):
        print(f"{self.name} is a {self.occupation}") #self calls the object on which method is called e.g. aditya

#creating a object
a = Details()
b = Details() #If no value is defined default will be considered i.e Vedant
a.name = "Aditya"
a.occupation = "AI student"

a.info()
b.info()
