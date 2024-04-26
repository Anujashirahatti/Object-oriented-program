class Student:
    def __init__(self,name,roll_number,password):
        self.name=name#public attractive
        self._roll_number=roll_number #protected attribute
        self.__password=password #private attribute
    def display_details(self):
        print("name",self.name)
        print("rollnumber",self._roll_number)
# private attribyte accessed within the class
        print("password",self.__password)
# Getter method for accessing private attribute
    def get_password(self):
        return self.__password
# setter method for modifying private attribute
    def set_password(self,new_password):
        self.__password=new_password
student=Student("alice","A001","secure_password")
print("name(public):",student.name)
print("rollnumber(protected)",student._roll_number)
print("password(private):",student.get_password())
student.set_password("new_password")
student.display_details()


    
