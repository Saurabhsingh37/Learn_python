# simple function of sum two number 
def Sum(a,b): # a and b is parameter 
    a = a+b
    return a
print(Sum(4,8)) # pass argument

# in this python two types functions user define and builtin function 
# built in function 
# print ()
# range()
# type()
# len()

def len_list(lst):
    print(len(lst))
user_input = input("enter data ")
u_list = user_input.split()
len_list(u_list)
print(type(u_list))


# join and split functions 
a = [2,3,4,6,8]
b = map(str , a)
c = ("  ".join(b))
print(c)
print(c.split("  "))


# # using empty list user input 
def fun(): 
    user = []
    b= (input("enter number b : "))
    c= (input("enter number c : "))
    d= (input("enter number d : "))
    a= (input("enter number a : "))
    user.append(a)
    user.append(b)
    user.append(c)
    user.append(d)
    print(user)
fun()


# find avg from user input 
def avg (a,b,c):
    sum = a+ b+ c
    average = sum / 3
    print("Average of your numbers : ",average)
p= int(input ("enter number a :"))
q = int(input("enter number b : "))
r = int (input ("enter number c :"))
avg(p,q,r)


# find infinite times odd and even number function 
def check_parity(number):
    if number % 2 == 0:
        print("EVEN:")
    else:
        print("ODD")
while True:
    a = int (input("enter your  number "))
    check_parity(a)
    


# recursive function 
def show(n):
    if (n==0): # base case 
        return 
    print(n)    
    show(n-1)
show(7) #function call


# factorial number using recursion 
def fact(n):
    if(n==1 or n==0):  # base case 
        return 1
    else:
        return n * fact(n-1)  # recursive function 
print(f"factorial number of is : ",fact(5))    



# wa function to calculate the sum of first n natural numbers 
def Nsum(n):
    sum = 0
    if n<=21:
        for i in  range(1,n+1,1):
            print(f"{sum}+{i}",end=" :")
            sum= sum+i
            print(sum)
    else:
        print("you enter wrong number : ")
a= int  (input("enter your number "))
Nsum(a)   


# using recursion
def sum(n):
    if(n==0):
        return 0
    print(f"{n}+{n-1}",end=" ")
    return sum(n-1)+n

a= sum(5)
print("sum of number ",a)   



#print user input list element 
def lis():
    lst = []
    while True:
        i = int (input("enter your number : "))
        lst.append(i)
        print(lst)
        if i== 20:
            return    
lis()   


# write a recursive function to print all element in a list 
def print_ele(lst,ind=0):
    if(ind==len(lst)):
        return
    print(lst[ind])
    print_ele(lst,ind+1)
a= [ "apple", "banana", "mango", "orange"]
print_ele(a)        

