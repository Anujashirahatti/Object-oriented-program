from abc import ABC, abstractmethod

class AbstractDetails(ABC):
    def __init__(self,user_name,pin,password):
        self.user_name=user_name
        self.pin=pin
        self.password=password
        
    @abstractmethod
    def display_details(self):
         pass