#  using property - we use the property decorator on any method in the class to use the method as a property :or updating value to another method 
class Result :
    def fifth(self , hindi ,english ,math):
        self.hindi = hindi 
        self .english = english 
        self .math = math 
    @property
    def percentage(self ):
        return str((self.math + self.hindi + self.english ) / 3 )+ "%"       

stu1 = Result()
stu1.fifth(50,50,50)

print(stu1.percentage)

stu2 = Result()
stu2.fifth(80,80 ,80)

print(stu2.percentage)

stu1.fifth(85,85,85)
print(stu1.percentage)  # updating percentage according to numbers 

