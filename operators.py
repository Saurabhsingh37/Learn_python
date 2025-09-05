# Arithmetic operator 
#Addition(+) 
a = 10 
b = 10
sum = a + b
print("sum of a and b : " ,sum)

#Subtraction (-)
sub = a - b
print("subtraction of a and b : " , sub)

#multiplication(*)
mul = a*b
print("multiplication of and b : " , mul)

#Division (/)
div = a/b
print("division of a and b : " , div)

#Modulus(%)
mud = a % b
print("Modulus of and b : " , mud)

#Exponentiation (**)
print(a**b)

#floor division 
s = 7
o = 3
print("floor division",s // o)




# ------ comparison operator


# equal to (==)
print("a equal too b : " , a==b)

# not equal too (!=)
print ("a not equal too b is : ",a!=b)

# grater then ( > )
print ("a grater then b is :", a>b)

# less then (<)
print ("a less then b is : ", a<b)

# grater then equal too and less then equal too .

print("s less then equal too o is : ", a<=o)
print ("s greater equal too  o is :",s>=o)




# -------logical operator 

# logical and (and &)
if (a and b == 10):
    print(" a and b value is equal : ")
#or operator (or ||) 
if(s or o == 7):
    print("one string value is 7 ")
# not operator (not !)
print("a not equal to b : ",a != b)  



# --------assignment operator
# 1) =
# 2) += 
# 3) -=
# 4) %=
# 5) /=
# 6) **=
# 7) //=      



# -------membership operator 
# in and not in .

a= [2,3,4,5,6,7]
print("check a have number 5 is :",5 in a )
print ("check a have not number 5 :", 5 not in a)



# --------identity operators:
# is and not is 

print ("check a is equal too b is : ", a is b)
print ("check is a not is b is : ", a is not b)


