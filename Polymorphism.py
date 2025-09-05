#  polymorphism / operator overloading - when the use same operator is called is allow to have different meaning according to the context 

# operator and driver 
# a+b  - addition  a.__add__(b)
#  a-b - subtraction  a.__sub__(b)
#  a*b - multiplication a.__mul____(b)
#  a/b - division a.__truediv____(b)
# a%b - modulus a__mod____(b)
# ___   ____ this is called a dander function 

# using same operator but meaning are different different 
print (1+2) #3
print ("Hindus" + "tan") #concatenate 
print([1,2,3]+[4,5,6]) #merge 


# complex numbers 2i _3j 
# addition of two complex number using dander function

class Complex :
    def __init__(self ,real ,imag):
        self .real = real
        self.imag = imag
    
    def show_number (self):
        print (self.real , "i +" , self.imag , "j")
    
    def __add__(self,num):
        newReal=self .real + num.real
        newImag = self.imag + num.imag    
        return Complex(newReal ,newImag)
num1 = Complex( 1,3)
num1.show_number()    

num2 = Complex(2,4)
num2.show_number()

num3 = num1+num2
num3.show_number()