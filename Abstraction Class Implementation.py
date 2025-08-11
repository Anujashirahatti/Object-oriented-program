
from abc import ABC,abstractcmethod
class Animal(ABC): 
    @abstractcmethod
    def eat():
        pass
    @abstractcmethod
    def color():
        pass
class Lion(Animal):
    def eat():
        print("lion can eat meat")
    def color():
        print("yellow")

class dog(Animal):
    def eat():
        print("dog can eat pedegree")
    def color():
        print("Black")
lobj=Lion
lobj.eat
lobj.color
