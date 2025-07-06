# ----set is a collection of unordered items 
# ---set is a mutable but its element are immutable and each element are unique 

nul_set =  set() # empty set syntax 

set1 = {1,2,3,6,9}
print (type(set1))
print ("this is a set : ", set1)
for i in set1:
    print(i)

set2 = { 2,5,4,2,4,2,"name","city"}
print("print second set : ",set2)

# --method of set 

set2.add("village")
print("add new element village ", set2)

set2.remove(2)
print("remove element 2 : ",set2)

set2.pop()
print("pop a random element : ", set2) # remove automatic first element of set 

set2.clear()
print("clear all set data : ")

#----- joints 

a = {2,2,4,3,5,6}
b = {5,8,9,2,1,4}
print ("joint of set1 nad set2 : ",set1.union(set2))
print("join set a and set b : ",a.union(b) ) # skip duplicate value

print("a intersection b is : ",a.intersection(b)) # return common valuer and ignore duplicate value


