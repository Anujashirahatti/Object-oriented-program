class Father:
    def sleep(self):
        print("can sleep at night 10:00pm to 5:00am")
    def eat(self):
        print("can eat")
        
class son(Father):
    def sleep(self):
        super().sleep()
        print("can sleep at night 11:00pm to 7:00am")
d=son()
d.sleep()        
d.eat()