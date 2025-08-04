# open file data 
f = open ("file.txt","r")
data = f.read()  # print all file data 
print(data)
print (type(data))
f.close()


# read file single line 
f2 = open ("file.txt","r+")
line1 = f2.readline() # print single line of file 
print(line1)
line2 = f2.readline()
print (line2)
f2.close()

# 'a' = append data or add data to end 
# 'w' = write data to hidden old data or override data 


#open file write mood and hidden old data or write new data 
f3 = open("file.txt",'w')
f3.write(" hellow gys my name is jonny and you .")
print(f3)
f3.close()


# open file to append "a" mood add  data  to end of the old data 
f4 = open ("file.txt", 'a')
f4.write("\n a learn to python early stage .")  # write new data 
print (f4)
f4.close 


# if open file in  append and write mod and file  not exist so python automatically create file by enter you file name . 
f5 = open ("python.txt","w")
# f5 = open ("python", "a")
f5.write("i create a python name file : ")
print (f5)
f5.close()


#  using with keyword perform file operations 
with open("file.txt" , "r") as f:
    data = f.read()
    print(data)

with open("file.txt" , "r+") as f :
    data = f.write("hey gys python is a very exciting language")
    print(data)
    
with open ("file.txt", "r") as f:
    data = f.read
    print(data)
    
    
# removing file using os module os library importing 
import os 
os.remove("UBTER Counselling1.pdf")    