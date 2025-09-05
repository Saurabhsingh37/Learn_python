# ------ Single line nad multiline string 
name = "Saurabh singh"
address = """ 
uttarakhand chamoli nandanagar
waduk gulari 
"""
print (address)
print (name )



# -------String Indexing
text = "Python"
print("display first character ", text[0])
print("display second character ", text[1])
print("display index 1 to 5 character ", text[1:5])
print("display last character in text ", text[-1])

# print single character
print(" python ")
for i in text:
    print(i)



#------string formating .formate() methoud
name = "saurabh"
age = 22

print("my name is {} i am {} year old : " .format(name,age))

print("hellow {1} how are you {0}" .format("jhon","hellow"))

print("my vilage name is {village},and city is {city}" .format(village = "waduk",city = "nandanagar"))

# string formate (formatted string Literals)
print(f"my name is {name}  and i am is {age} year old :.")
a = 5
b = 5
print (f"sum of {a} and {b} is : {a+b}")


# padding and alignment..
print(f"{text:>10}") #left align
print(f"{text:<10}") #right align
print (f"{text:^10}") #center align

# -----change string case 
case = " saurabh singh "
print ("change case : ",case.upper())
print (" change case : ", case.lower())
print (" change case : ", case.capitalize())
print (" change case : ", case.title())

# -----removing Whitespace 
print("removing whitespace : ",case.strip())
print("removing left whitespace : ",case.lstrip())
print("removing right whitespace : ",case.rstrip())


# -------replace string 
replace = "python is fun "
print ("finding  text index is : ",replace.find("fun"))
print ("replace selecting text is : ",replace.replace("fun" , "awesome"))


# ------finding length of string using  -> len() function 
print (" length of replace string - : " ,len(replace))



# ----- .join() and .split() function
texts="apple , banana , orange"
sptexts = texts.split("@")
print("split text -: ",sptexts)

jointxt= " @ ".join(sptexts)
print("join sptexts -: ",jointxt)



# ----string slicing
print("string slicing -: ",replace[::2])
print(replace[0:]) # 0 index to last 
print(replace[:5]) # starting to 5 index 
print(replace[:-1]) # reverse indexing 
print(replace[::-1]) # reverse string 


# --------more functions in python 
str.endswith("bh") #return true if end of string is bh world 

str.capitalize() #first word is capitalize 

str.replace("old ", "new")#replace sentence

str.count ("saurabh") #count selected sentence 

str.find("word") #find selected word in sentence