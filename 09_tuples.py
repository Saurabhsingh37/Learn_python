# -----tuples are immutable these value are not changed 
tup = ("saurabh ",5,6)
print (tup)

print ("print first index value in tuple : ", tup[0])
print ("print last element of tuple : ", tup[-1])

# tup[-1] =68 # this is not allowed in python 
# ---- tuple methods 
print("count specify element : ",tup.count(5))

print ("find index of first occurrence", tup.index(5))
# end.
