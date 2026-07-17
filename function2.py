
# take user input data in list integer form and print length of list :

# def length(data):
#     print(len(data))

# data = []

# while True:
#     a= input("enter your data:")
#     if a.lower() == "e":
#         break
#     # it is not work because here we need to used try and catch methods 
#     # if a != int (a):
#     #     print("please enter only numbers")
#     #     break
    
#     data.append(int(a))
# print("length of data: ", end=" ")
# length(data)    
    


#  using split() string into list converting method

# def length ( data):
#     print(len(data))
#     print(data)

# num = input("enter your data :").split()
# length(num)


# exit when press enter means empty input not except 

# def info( data):
#     print(data)
#     print(len(data))

# lis = [] 
# while True:   
#     a = input("Enter your element : ")
#     if a == "":
#         break
#     lis.append(int(a))
# info(lis)    


# write an function print element in single line 
data = [ 1,2,3,4,5]
def element(data):
    for i in data:
        print(i, end=" ")
# element(data)

# Factorial program 
n= 5
def fact (n):
    fact = 1
    for i in range(1, n+1 , 1):
        fact *= i
    print("your factorial number is ", fact)
# fact(n)  

# currency convertor  function 
dollar = 50
def convert(usd):
    print("Rup",usd * 95.41)
# convert(dollar)


# find  number even or odd
def check():
    while True:
        num = input("Enter your number :")
        if num == "e":
            break
        num = int(num)
        if num % 2 == 0:
            print("Even number : ",num)
        else: 
            print(f"Odd number : {num}")    
# check()        


# input two number and 
# def sum (num_a , num_b):
#     return num_a +num_b
# a= int(input("Enter your first number:"))
# b= int(input("Enter your second number :"))
# print(sum(a,b))

# default argument function 

def intro(name, age, city="Chamoli"):
    print("\n------ Student Details ------")
    print(f"Student Name : {name}")
    print(f"Student Age  : {age}")
    print(f"City         : {city}")
    print("-----------------------------")


while True:
    name = input("Enter student name (or 'exit' to quit): ")

    if name.lower() == "exit":
        break

    age = input("Enter student age: ")

    city = input("Enter student city (Press Enter for default): ")

    if city == "":
        intro(name, age)          # Uses default city
    else:
        intro(name, age, city)    # Uses entered city


