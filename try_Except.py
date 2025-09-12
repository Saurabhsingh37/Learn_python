'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code,regardless of the result of the try -and except blocks.
'''

# The try blok will generated an exception ,because x is not define .

try:
    print(x)
except:
    print("An exception occurred")
    '''
    Since the try block the program will crash and raise an error:
    Without the try block ,the program will crash and raise an error:
    '''
    
    # Else : You can use the else keyword to define a block of code to be executed if no error were raised:
    
    try:
        print("hello")
    except:
        print("Something went wrong")
    else:
        print("Nothing wrong ")
        


#  Finally : The finally block ,if specified will be executed regardless if they try block raised an error or not .

try:
    print(x)
except:
    print("Something went wrong")
finally:
      print("The 'Try except ' is finished")
      
# Try to open and write to a file that is not writable:
try:
    f= open("demofile.txt") 
    try:
        f.write("luurom Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.closed()
except:
        print("something went wrong the opening file :")
        
        
        
# Example a atm program 

try:
    amount = int(input("Enter amount: "))
    if amount > 10000:
        raise ValueError("Limit exceeded!")
except ValueError as e:
    print("Error:", e)
else:
    print("Withdrawal successful!")
finally:
    print("Transaction complete.")
 
        