#  Define a circle class to create a circle with radius r using the constructor define an Area() method mof the class which calculate the area of the circle .Define a perimeter() method of the class which allows you to calculate the perimeter of the  circle .

class Circle :
    def __init__(self , radius):
        self .radius = radius 
    
    def area(self ):
        area = (22/7) *self.radius **2
        print ("area of circle : ",area)
    
    def perimeter (self)    :
        perimeter = 2 * (22/7) *self.radius 
        print("perimeter of circle : ",perimeter)
        
cr = Circle(2)
cr.area()
cr.perimeter()        



# Define a Employee class with attribute role department & salary.This class show detail method.
# create an engineer class that inherits properties from Employee & has additional attribute : name &age ?

class Employee:
    def __init__(self , role ,dept, salary) :
        self . role = role 
        self.dept = dept
        self.salary = salary
    def showDetail(self):
        print ("role : ", self.role)
        print("department : ", self.dept)
        print("salary: " , self.salary)

class Engineer(Employee) :
    def __init__(self,name ,age):
        self.name = name 
        self.age = age
        print("name : ", self.name)
        print("age : ", self.age) 
        super().__init__("ds","sw",2322)
        
E1= Employee("manager", "finance",24000)
E1.showDetail()  

f = Engineer("saurabh",45)
f.showDetail()      