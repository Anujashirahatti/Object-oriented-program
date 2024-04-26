class ComplexNumber:
    def __init__(self,real,image):
        self.real=real
        self.image=image
        
    def __add__(self,others):
        return f"{self.real+others.real}+{ self.image+self.image}i"
    
c1=ComplexNumber(3,4)
c2=ComplexNumber(1,2)

print(c1+c2)

