'''
json is a syntax for storing and exchanging data .
JSON is tex, written with javaScript object notion .
python has a built -in package called json . witch can be used to work with json data .
'''
# Convert from json to python : 
import json 
# some json 
x = '{"name":"jhon","age":30,"city":"new york"}'
# parse X:
y = json .loads(x)
# The result is a python dictionary 
print(y["age"])
print(type(y))
print(type(x))


# Convert from json to python 
'''
if you have a python object you can convert it into a json by using json.dumps() method.
'''
import json
# a python object (dict):
x = {
    "name":"saurabh",
    "age":"40",
    "city":"uttarakhand"
}
# convert into json
y = json .dumps(x)
print ("json dict",y)
print(type(y))

# YOU CAN CONVERT PYTHON OBJECT OF THE FOLLOWING OF THE FOLLOWING TYPES,INTO JSON STRING :
'''
dict
list
tuple 
string
int
float
True
False
None
'''
# CONVERT PYTHON OBJECT INTO JSON STRING ,AND PRINT THE VALUES:
import json 

print(json.dumps({"name":"saurabh","age":20}))
print(json.dumps(["apple","banana"]))
print(json.dumps(("apple","banana")))
print(json.dumps("hello"))
print(json.dumps(45))
print(json.dumps(31.89))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# CONVERTING PYTHON OBJECT CONTAINING AN THE LEGAL DATA TYPES :

import json

x = {
"name": "John",
"age": 30,
"married": True,
"divorced": False,
"children": ("Ann","Billy"),
"pets": None,
"cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
]
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

# The json .dumps method has parameter to make it easier to read the result:


''''
REAL LIFE EXAMPLE: Imagine you order food using Swiggy/Zomato 
When you select food item ,the app need to send your order detail to the server. 
but python dictionary cannot be directly sent over the internet.
so we convert it into JSON format (like a universal text format:)
This JSON data is sent to the server -> server understands it -> processes your order.
JSON in python is used to store ,share,and exchange data. ex. amazon social media instagram facebook etc.
'''
import json

# Python dictionary (order details)
order = {
    "customer": "Saurabh",
    "items": [
        {"name": "Pizza", "quantity": 2, "price": 250},
        {"name": "Coke", "quantity": 1, "price": 50}
    ],
    "total": 550,
    "delivery": True
}

# Convert Python dict → JSON (string)
json_data = json.dumps(order)
print("JSON Format:", json_data)

# Save JSON to a file
with open("order.json", "w") as file:
    json.dump(order, file)

# Read JSON from file
with open("order.json", "r") as file:
    loaded_order = json.load(file)
    print("Loaded Order:", loaded_order)


