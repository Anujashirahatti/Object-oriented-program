class Circle:
    pi=3.14 #class object
    def __init__(self,radius):
        self.radius=radius
        self.area=self.pi*radius*radius
        
    def circumference(self):
        circum= 2 *self. pi* self.radius
        return circum
    
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        a= self.length * self.width
        return a
    
circle_1=Circle(4)
print("circle 1 circumference",circle_1.circumference())
print("circle1 area",circle_1.area)

circle_2=Circle(14)
print("circle_2 of circumference", circle_2.circumference())
print("circle_2 of area is",circle_1.area)

Rectangle_1=Rectangle(4,4)
print(Rectangle_1.area)
print(f"rectangle is {Rectangle_1.area()}")


        
        
    