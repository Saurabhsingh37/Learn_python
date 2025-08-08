# encapsulation ---->
# Wrapping data and function in a single unit .

# Create Account class with 2 attribute -Balanced and Account no.
# Create methods for debit credit & print the balanced. 
class Account:
    def __init__(self , bal,acc):
        self.balanced = bal
        self .account_no = acc
    
    def debit(self,amount):
        self.balanced -= amount
        print("Rs.",amount,"was debited")
        print("total balanced " , self.get_balanced())
        
    def credit(self,amount):
        self.balanced += amount
        print("RS.",amount, "was debited")
        print("total balanced = ",self.get_balanced())

    def get_balanced(self):
        return self.balanced 
    
acc1 = Account(10000 ,1002003)
# print(acc1.balanced)
# print(acc1.account_no)
print(acc1.get_balanced())
acc1.debit(500)
acc1.credit(50000)