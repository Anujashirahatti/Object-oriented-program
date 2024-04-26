#INHERITENCE

class human:
    def __init__(self,hobby,food):
        self.fav_hobby=hobby
        self.fav_food=food
        
    def display_info(self):
        print(f"she plays {self.fav_hobby},and he likes {self.fav_food}")
  #call function from above datas       
class learn(human):
    def __init__(self,hobby,food,language):
        super(). __init__(hobby,food)#super().is keyword
        self.fav_language=language
    def display_info(self):
        super().display_info()
        print(f"language she speaks {self.fav_language}")
user=learn("series","movie","kannada")
user.display_info()


        
        
        
          