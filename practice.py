data = (1,2,4,3,2,4,5,43,3,2,4)
ind = 0
number = int (input("Enter your number "))

while ind <= len(data)-1:
        
        if data[ind] == number:
                print(f"found number is index {ind}")
        print("finding......")
        ind += 1
