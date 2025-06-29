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
    


#using break in loops 
print ("using break condition :")
for i in range(20):
    if(i%2==0):
        continue
    print(i)
    if(i==15):
        break

    