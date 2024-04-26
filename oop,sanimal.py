class animal:
    def __init__ (self,name,size,legs):
        self.animal_name=name
        self.animal_size=size
        self.animal_legs=legs
    def sound(self):
        print('louder sound')
        
    def count_leg(self):
        if self.animal_legs>0:
            print("land animal")
        else:
            print("Water animal")
        
    def print_animal(self):
        print(f"Elephant is {self.animal_name,self.animal_size,self.animal_legs}")
        print(f" dog has{self.animal_size,self.animal_name,self.animal_legs}")
        print(f"panda has{self.animal_legs,self.animal_name,self.animal_size}")
    
    def classify_animal(self):
        if self.animal_legs==0:
            print(animal,"is water animal")
        else:
            print(animal,"is land animal ")


n=input('Enter the classifly_animal names')
        
Elephant=animal('fat','larger',4)
panda=animal('cutie','small',4)
dog=animal('bark','thin',4)
fish=animal('gold_fish','small', 0)

if n.lower() == 'elephant':
    Elephant.classify_animal()
elif n.lower() == 'panda':
    panda.classify_animal()
elif n.lower() == 'dog':
    dog.classify_animal()
elif n.lower() == 'fish':
    fish.classify_animal()
else:
    print(f"Animal '{n}' not found.")

        
