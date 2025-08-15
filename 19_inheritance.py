# inheritance -> inherit property in  parents class to child class 


class Car :
    @staticmethod
    def start():
        print("your car was started : ")
    
    @staticmethod
    def stop ():
        print ("your car is stop :")    

class Toyota (Car): # inherit Car class 
    def __init__(self,name):
        self.name = name 
        print("fortune car 4*4:")
car1 = Toyota("Fortune")   
car1.start()  
car1.stop()   


# multi_level inheritance 
class New_branch(Toyota):
    @staticmethod
    def city():
        print ("new branch in Uttarakhand :")
    def register(self,name ):
        self.name = name 
        print ("your register city name is :" , name  )
customer = New_branch("name") 
customer.city()
customer.register("chamoli")  
customer. start()    


# multiple class inheritance  - many class property inherit a single child class 
class A : 
    print ("this is a class a : ")
class B :
    print("This is a class b")   
class C(A,B):
    print("This is class c")
    
obj = C()
        
        