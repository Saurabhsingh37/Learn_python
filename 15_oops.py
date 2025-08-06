# creating class and object 
class Car:
    name = "bmw"
a = Car()  
print(a) # print only object  location 
print(a.name) # print  object property


#  constructor - this is a first function of class and it is python automatically created and every object call first constructor or __init__ function in python . 

class Student :
    def __init__(self , name ):  #  class constructor 
        self.name = name  # self  is reference of object 
        print("this is class constructor:")

st1 = Student("saurabh")
print(st1.name)

st2 = Student("Gaurav")
print(st2.name)


#  define class attribute and instance attribute 
#  attribute = attribute is a variable or data 
class Student:
    name = "saurabh" # class attribute 
    def __init__(self , name , age): # class constructor 
        self.name = name  # object attribute
        self .age = age
        print("this is a class object ")
s1 = Student("Gaurav",45)  
print(s1.name ,s1.age)        # first priority is object attribute 


# method in class  or function 
class Village :
    def v_name (self):  #method in class as default method
        print("my village name is waduk")
    
    def v_festival(self,name): # perimeter method
        self.name = name 
        print("festival name : ",name)
v = Village()
v.v_name()
v.v_festival("vasantpanchami")



# Create student class that take name and marks of 3 subject as arguments in constructor then create a method to print the average marks ?
class Student ():
    def __init__(self , name , numbers):
        self . name = name 
        self . numbers = numbers 
    def average (self ):
        sum = 0
        for el in self.numbers:
            sum += el
        print ("hii", self.name,"your average number is : ",sum/3)    
student= Student("jon" , [20,30,50])
student.average()

student2 = Student("Gaurav" , [60,60,80])
student2.average()


#  Static method using decorator(@staticmethod) 
#  Decorator changed behaviour to function and modifying in this not using self keyword 
class Student : 
    @staticmethod
    def entry ():
        print("all students enter at 9:30 am ")
obj = Student()
obj.entry()