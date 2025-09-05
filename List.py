# ----------using list methoud and funtions 
lis = ["saurabh" , " gaurabh" , "adition" , 5 , 6 , 90]
print(lis)
print(type(lis))
for i in lis:
    print(i)

#list slicing ----

print ("print first element :",lis[0]) 
print ("print all element of list : ",lis[0:])
print (" print last element of list : ",lis[-1])
print ("print second to last element : ", lis[2:-1])

# --list methods
lis.append("singh")
print(lis) # add element to last index 

newlis = lis.copy()
print("list copy in newlis : ",newlis) # copy list in new memory location 

lis2 = [2,8,6,4,10,16,12]
lis2.reverse() # reverse list element 
print ("print list reverse : - ", lis2)
lis2.sort()# shorting list to ascending order
print("print list to asc order : ",lis2)
lis2.sort(reverse=True) # shorting list to desc order 
print ("print list to dsc order : ",lis2)
lis2.insert(3,20) # insert new element at index 
print(lis2)
lis2.remove(2)# remove element to first occurrence of element 
print (" removing element 2",lis2)
lis2.pop(3) # removing element at index 
print("removing element at index 3 : " ,lis2)

# ---in list many more methods . 