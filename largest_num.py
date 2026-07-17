numbers = [5,8,2,10,3,25,7]
largest = 0
for i in range(0,len(numbers)-1):
    if numbers[i] > largest:
        largest = numbers[i]
    # else:
        
print("Your largest number is :",largest)