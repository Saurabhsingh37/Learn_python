# create a new file flowing formate

data = open ("practice.txt", "w")
data.write (" Hi everyone \n" " We are learning File i/o \n"" Using java")
print(data)
data.close()


#  replace java to python --> note replacing word after do to open read mood file first 
with open ("practice.txt","r") as f :
    data = f.read()
    
d = data.replace("java" , "python") # replacing data 
print(d)

with open ("practice.txt" ,"w") as f : # write replacing data in file 
    f.write(d)
    print (d)

# find a random word using proper function indentation 
def find (word):
    with open ("practice.txt", "r") as f :
        data = f.read()
        if (data.find(word) != -1):
            print("find word")
        else:
            print("not found :")
find("saurabh")  



#check the first line existing word
def check_line ():
    word = " learning"
    data =  True
    line_no = 1
    with open ( "practice.txt" , "r") as f :
        while data:
            data = f.readline()
            if (word in data ):
                print (line_no)
                return
            line_no += 1
            
    return -1
check_line()        