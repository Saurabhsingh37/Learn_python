# ----create a student sata in dictionary form 
# dictionary are mutable data types and changed its values or manipulate 
dict = {"school" : "svm ghat",
        "name": "saurabh sing ",
        "class" : "12th",
        "city" : "nandanagar",
        "pincode": 246435
        }
print (type(dict))
print ("Your college data : ",dict)


# ---print specific key's value 
print("print pincode : ", dict["pincode"])
print ("print your name : ", dict["name"])

# --assign a new  value in keys 
dict ["name"] = "saurabh negi"
print ("changed name value",dict )

# nested dictionary

collage = { "name" : "saurabh ",
        "subject" : {
        "che": "02",
        "phy": 3,
        "math":5
        },
        "city": " haridware" 
}
print("print nested subject dictionary : ",collage["subject"])
print("print math value in nested dict : ",collage["subject"]["math"])

#----- method's
a= dict.keys()
print ("print all dictionary keys : ",a)

b= dict.values()
print (" print all values in dictionary : ",b)

c=dict .items()
print ("print all items in dictionary : ",c)

print("print specific key values : ", dict.get("name")) #this is a good method to return any values 

dict.update({"name":"saurabh singh negi"}) #override old values .
print ("update new value's : ", dict)

dict .update({"village":"rampur"})
print ("insert new keys value : ",dict)