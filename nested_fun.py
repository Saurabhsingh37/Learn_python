# 1
def outer():
    print("outer function start")
    def inner():
        print("inner function running")
    inner()    
    print("outer function is end")
outer()    


# 2
def out():
    def square(n):
        print(n*n)
    square(5)    
out()    

# 3
company = "Google"
def parent():
    name = "Saurabh"
    def inner():
        print("company : ",company)
        print("name :",name)
    inner()    
# parent()  


#  multiple inner functions 
def calculator():

    def add(a, b):
        return a+b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b
    def divide(a, b):
        return a / b

    # Call all four functions
    print(add(5,5))  
    print(subtract(5,5))
    print(multiply(5,5))
    print(divide(5,5))
calculator()    