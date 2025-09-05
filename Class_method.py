#  class method - class method is using to changed class attributes values 

class A : 
    name = "saurabh"
    print(name)
#  without using class method 
    # def change_name (self ,name ):  
        # self .name = name 
        # print ("changed your name : ",name) 
           
    @classmethod # using class method decorator 
    def change_name(cls,name):
        cls.name = name
        
p1 = A()
p1.change_name("saura")
print(p1.name    )
print(A.name)


#  python have a three types of method 
#  1)  Static method 
#  2) class method 
#  3) instance method