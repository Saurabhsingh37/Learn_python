# ---store following word meaning in a python dictionary 

dict = {"table": ["a pice of furniture","list of fact and figure "],
        "cat": " a small animal"}
print (type(dict["table"]))


# ------you are given a list of subjects for students assume one classroom is required for 1 subject . How many classrooms are needed by all students . 
subject = { "python", "java", " c++","python","javascript","java","python","java","c++","c"}
print("required classroom of every subject : ", len(subject))


# ----wap to marks of three subjects from the user and store in a dictionary start with an empty dictionary & add one by one use subject name as key & marks as value ?

marks = {}
a = int(input("enter chemistry numbers : - "))
marks. update({"chemistry": a})

b = int(input("enter physics number : - "))
marks.update({"physics":b})

c = int(input("enter math number : - "))
marks.update({"math":c})

print("your result : ",marks)