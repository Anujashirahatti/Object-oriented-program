from AbstractDetails import AbstractDetails

class Atm_card(AbstractDetails):
    def display_details(self):
        print("Atm_card Details:")
        print("user_name:", self.user_name)
        print("pin:", self.pin)
        print("__password:", self.__password)
        
    def get_password(self):
        return self.__password
    
    def set_password(self,new_password):
        self.__password=new_password
    
my_atm_card=Atm_card("anuja",1713,0000)
print("__password(private)",my_atm_card.password)
print("pin(private)",my_atm_card.pin)
