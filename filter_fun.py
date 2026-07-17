# # filter function used only select element in iteration apposite of map function 

# number = [3,4,5,6,3,2]
# fltr = list(filter(lambda ele : ele % 2 == 0 , number)) # if here we used map () so print only True and False 
# print(fltr)


# #  keep number grater than 4
# grater = list (filter(lambda ele : ele > 4 , number))
# print("grater than 4 : ", grater)


# # Remove empty string 
# data = ["saura","","gaura","king",""]
# filter = list(filter(lambda ele : ele != "",data))
# print(filter)

# # print number of divisible of 5 

num = [10,15,20,25,30,35,40]
d5 = list(filter(lambda n : n % 5 != 0 , num))
print(d5)


# grater than 50 number give student 5 number bonus
marks = [35, 80, 92, 45, 60, 28, 75]
passing_n = list(filter(lambda ele : ele >= 50 , marks))
total_n = list(map(lambda n : n + 5,passing_n))
print(total_n)