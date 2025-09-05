print("10th result grade : ")
number= int(input("enter your number:"))
if(450<=number & number <= 500):
    print("Excellent \n Grade = A+")
elif(400<=number & number < 450):
    print("Very Good \n A")    
elif(350<=number & number < 400):
    print("Good \n Grade = b")
elif(300<=number & number < 350):
    print("passed \n grade = c")   
else:
    print("you are not promote \n Try again :")  
print("Thank You:")           