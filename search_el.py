data = (2,4,3,5,6,8,9,7,6,7)

while True:
    ind = 0
    count = 0
    search = input("Search your number or exit :")
    if search == "exit":
        break
    search = int(search)

    while ind <= len(data)-1:
        if search == data[ind] :
            print(f" Your search number : index {ind} : {data[ind]}")
            count +=1
        ind +=1
    print(f"Search number exist :{count} times")  
    if count == 0:
        print("Your number is not exist : ")  
    