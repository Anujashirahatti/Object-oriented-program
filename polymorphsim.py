class Animal:
    def speak(self):
        return "animal makes a sound"
    
class dog(Animal):
    def speak(self):
        super().__init__()
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class Cow(Animal):
    def speak(self):
        return "Moo!"
    
    
def make_animal_speak(animal):
    print(animal.speak())
    
Dog=dog()
cat=Cat()
cow=Cow()
make_animal_speak(Dog)
make_animal_speak(cat)    
make_animal_speak(cow)
    
    