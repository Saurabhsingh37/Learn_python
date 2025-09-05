# ------for loop in python
details = ["name - ", "age - ", "date - ", "city -"]
for student in details:
    print(student)


#-------for loop using range function  
for i in range (11,20,2): #(11 - starring , 20 - end , 2 - gap )
    print (i)
    


#------while loop 
count = 0
while count <= 20:
    print(count )
    count +=1
    


#using break ans continue in loops 
print ("using break condition :")
for i in range(20):
    if(i%2==0):
        continue # skip 
    print(i)
    if(i==15):
        break #stop 


# print number 1 to 10 using while loop 
print("\n1 to 10 : - ")
i = 0 
while i<= 9 :
    i+=1
    print(i)

    
# -----print multiplication table of a number  
a =  int (input("enter your number : - "))
print(f"your table of {a}")
b=0
while b<=9:
    b+=1
    print(f"{a} * {b} = ",a*b)


# ---print list element using while loop

number = [ 1,2,3,4,5,7,8,10,5]
i = 0 
while i < len(number):
    print("element:",number[i],  "index : ",i)
    i+=1
    
    
# searching a number x n this using loop while 
x= 5
i =0 
while i< len(number):
    if(number[i]==x):
        print("find your number index : " ,i)
    else:
        print("finding again : ")
    i+=1        
    

# Search for a number x in this tuple using loop 

x = 10
i=0
a = [2,5,4,3,6,8,10,12,15,9,10]
for el in a :
    if(el==x):
        print ("your element is found",i)
    i+=1
else:    
    print("searching again ")
    

# ------using pass is  a null statement 

for i in range():
    pass  # null argument using this feature future