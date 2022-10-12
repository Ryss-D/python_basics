from typing import List

class Student: 
    def __init__(self, name: str, grades: List[int] = []): #This is bad!
        self.name = name
        self.grades = grades

    def take_exam(self, result:int):
        self.grades.append(result)

bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
##pherhaps we are not assigning any grade to rolf
##if we print rolf.grade it will return the bob grade
##that becasuse we are using mutables as default
##and python its reusing the default object (that mutate previuly)
##(same place in memori if we print id(object))
##for the new object creation
print(rolf.grades)

##A better aproach for this will be

from typing import List, Optional

class Student: 
    def __init__(self, name: str, grades: Optional[List[int]] = None): #This is bad!
        self.name = name
        ##if no grades or grade == None will use empti list
        self.grades = grades or []

    def take_exam(self, result:int):
        self.grades.append(result)

bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)