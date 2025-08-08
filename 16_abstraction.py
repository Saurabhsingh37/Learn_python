# Abstraction - Hiding the implementation detail of a class and only showing the essential feature to the user . 

class Car :
    def __init__(self):
        self .acc =  False
        self . brk = False
        self .clutch = False
    
    def start (self):
        self.clutch = True
        self.acc = True
        print("Car started..")  # this is all hiding data show only essential part 

car1 = Car()
car1.start()     
