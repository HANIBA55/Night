class Person:
    def __init__(self,Fname,Lname):
        self.fristname = Fname
        self.lastname  = Lname
        
    def printname(self):
        print(self.fristname , self.lastname)

class Student(Person):
    def __init__(self, Fname, Lname):
        Person.__init__(self,Fname,Lname)

x = Student("Mick","Olsen")
x.printname()
        