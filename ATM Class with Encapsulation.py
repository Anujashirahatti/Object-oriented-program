
class ATM:
    def __init__(self):               
        self.name="Anu"
        self.__pin=7019  #private
        self._card="SBI" #protected
        self.balance=10000

        
    def setpin(self,newpin):
        self.__pin=newpin
        
    def getpin(self):
        return self.__pin
    
    def deposite(self,amount):
        self.balance+=amount
        print(self.balance)
        
    def withdraw(self,ammount):
        if ammount<=self.balance:
            self.balance-=ammount
        else:
            print("insufficent Funds")
            
obj=ATM()
print("old pin")
print(obj.getpin())

obj.setpin(1234)
print("new pin")
print(obj.getpin())
print(obj._ATM__pin)

obj.deposite(50000)
print("new balance")
print(obj.balance)
obj.withdraw(500)
print("After withdraw balance is")
print(obj.balance)
