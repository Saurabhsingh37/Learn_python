number = int(input("enter your number \n belongs to less then of 6 :"))

if (number <=6):
    match number :
        case 1:
            print("One")
        case 2:
            print("Two")    
        case 3:
            print("Three")    
        case 4:
            print("four")      
        case 2:
            print("Five")          
        case 6:
            print("six")        
        case _:
            print("reenter your number :")
            
else:
    print("Enter your valid number : ")                
            