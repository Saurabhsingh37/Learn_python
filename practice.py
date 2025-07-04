# # write a program to user enter a first name and print its length ?
# f_name = (input ("enter your name : "))
# print("length of your name : ",len(f_name))
# print ("find lastname ",f_name.find("singh"))
# print("your name end is singh :- ",f_name.endswith("singh")
# )

# print(f"your name is {f_name} negi")
# print ("count your name in s -: ",f_name.count("s"))


# ----check number is odd or even 

# number = int (input ("Enter your number : - "))
# if (number % 2==0 ):
#     print ("your number is even ")
# else:
#     print (" your number is odd ")



# -----find the greater number of 3 number enter by user .

first  = int (input("enter number first : - "))
second= int (input ("enter number second : - "))
third =int (input("enter number third : - "))

if(first >second and first >third):
    print("first is greater number : ")
elif(second > first and second > third):
    print("second number is greater number : ")
elif(first == second and first == third & second == third):
    print ("all number are equal : ")        
elif(third > first and third >second):
    print("third number is greater : ")    
else:
    print("you enter two number same or  other : ")

