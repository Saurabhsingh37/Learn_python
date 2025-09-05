# # using del keyword in class objects 
# class Student :
#     def __init__(self, name):
#         self. name = name
#         print(" using dell keyword :",name)
# stu= Student("saurabh")
# print(stu.name) 
# del stu # delete object 
# print(stu.name) #display error



# private method and attribute 
# this is accessible only inside of same class 
class Bank:
    def __init__(self, acc,pas):
        self.acc = acc  # public attribute 
        self.__pas = pas # private attribute 
    def access(self):
        print("your account no",self.acc)
        print("your password",self.__pas)
        
    def reset_pas(self,np): # accessing private attribute 
        self.__pas = np
        print(self.__pas)
        
    def __new1_cus(self, name): # private method
        self. name = name 
        print ("Your name : ",name ) 
    def welcome(self,name):  # accessing private method
        self.__new1_cus(name)       
        
cus = Bank(1002003 , 786786)
cus.access()
# print(cus.__pas) # not accessible
print (cus.acc)
cus.reset_pas(3233) # private attribute access using method 
cus.welcome("saurabh")

        