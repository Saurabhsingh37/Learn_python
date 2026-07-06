data = (1,2,4,3,2,4,5,43,3,2,4)
while True:
    number =  input("Enter your number ")
    if number == "exit":
        break
    number = int(number)
    ind = 0

    while ind < len(data):
        if data[ind] == number:
                print(f"found number is index {ind}")
        else:
            print("number not found")
        ind += 1
print("Program end : ")