# recursion is a method of call function itself repeatll 

# print 10 to 1

def rec (n):
    if n == 0 :
        return

    print("up" ,n)
    rec(n-1)
    print( n)
    print("down")

# rec(10)  

# factorial number print 
# def fect (n)  :
#     if (n == 1 or n == 0):
#         return 1
    
#     return fect(n-1) * n
# ans = fect(5)
# print("FActorial number : ", ans)


# calculate sum of first n natural  number 
def sum_n(n):
    if n == 0:
        return 0
    return sum_n(n-1) + n
# print(sum_n(5))


# power of n numbers 
# def power(num , pow):
#     if pow == 0 :
#         return 1
#     return(num * power(num, pow-1))
# num = int (input("enter your number :"))
# pow = int(input("Enter power of number : "))
# print("Square of these number : ",power(num,pow))


# digit counting program 

def d_count(num):
    if num == 0:
        return 0
    return 1+ d_count(num // 10)
# print(d_count(1234))


# reverse number 
def reverse(num):
    if num == 0:
        return ""
    return str(num % 10) + reverse (num// 10)
# print(reverse(12345))

# print all element of the list 
def element(lis, ind):
    if ind == len(lis):
        return 
    element(lis, ind+1)
    print(lis[ind])

element([1,2,3,4,5],0)

