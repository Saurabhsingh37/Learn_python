
# use super keyword - accessing parent constructor or method in child class 
class School :
    def __init__(self, name, place ):
        self.name = name
        self.place = place
    def course(self):
        print("all engineering course available")    

class Student (School):
    def __init__(self,pin,name,place):
        super().__init__(name,place)
        self.pin = pin 
        print("pic code : ",pin)
        print (f"your School name {name} and your city {place}")
        super().course()

school = Student("89","gkv","haridwar") 
# school.course()       