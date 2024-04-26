from Abstractanimal import Abstractanimal

class pikachu(Abstractanimal):
    def display_details(self):
        print("pikachu details:")
        print("color:",self.color)
        print("number of legd",self.num_leg)
        print("tail",self.tail)   
class panda(Abstractanimal):
    def display_details(self):
        print("panda details:")
        print("color",self.color)
        print("number of legs",self.legs)
        print("tail",self.tail)       
class Elephant(Abstractanimal):
    def display_details(self):
        print("Eleohant details:")
        print("color",self.color)
        print("number of legs",self.legs)
        print("tail",self.tail)
class cow(Abstractanimal):
    def display_details(self):
        print("cow details:")
        print("color",self.color)
        print("number of legs",self.legs)
        print("tail",self.tail)
class Tiger(Abstractanimal):
    def display_details(self):
        print("Tiger details:")
        print("color",self.color)
        print("number of legs",self.legs)
        print("tail",self.tail)