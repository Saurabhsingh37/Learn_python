print("print table 1 to 100")

a = int (input("enter number : "))
if a <= 100:
    for b in range(1,11,1):
        c=a*b
        print(c)
else:
    print("this number above of 10 : \n enter new number less then of 10 :")
