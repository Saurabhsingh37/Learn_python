n = 1
count = 0
total_count = 0

while n<= 85:
    if n % 2 == 0:
        # print(n)
        count +=1 
        
    n+=1
    total_count += 1
print("Even numbers ",count)
print("odd numbers : ",total_count-count)
    