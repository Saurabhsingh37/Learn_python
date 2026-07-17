# # lambda function 
# data = ['1','2','3','4','5']
# new_data = tuple(map(int,data))
# print(new_data)
# print(type(new_data)) 

# # Add two list element 
# a = [1,2,3,4]
# b = [4,3,2,1]
# result = list (map(lambda x,y: x+y ,a,b))
# print(result)

# # print string single element 
# name = "SaurabhSingh"
# show = list(map(print,name))

# # convert to upper case
# upper = list(map(str.upper,name))
# print(upper)


# # add text to every character 
# txt = list(map(lambda ch:"Later:" +ch,name ))
# print(txt)

# # convert to lower case 
# lower = list(map(str.lower,name))
# print(lower)

# # find maximum number 
# num = ['1','4','2','6']
# maximum = map(int, num)
# print(max(num))



# Double every element 
ele = [1,2,3,4,5]
ele2 = list(map(lambda i : i + i+i, ele))
print(ele2)