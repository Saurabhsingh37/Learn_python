print("print table 1 to 10")

a = int (input("enter number : "))
if a <= 10:
    for b in range(1,11,1):
        c=a*b
        print(c)
else:
    print("this number above of 10 : \nenter new number less then of 10 :")
