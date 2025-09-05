# A DATE IN PYTHON IS NOT A DATA TYPE ITS OWN BUT WE CAN IMPORT A MODULE DATETIME TO WORK WITH DOTES AS DATE  OBJECTS.

# IMPORT THE DATETIME MODULE AND PRINT CURRENT DATE 
import datetime as dt
x = dt.datetime.now()
print ("Today :",x)


# Return the year and name of weekday
import datetime 
x = datetime.datetime.now()
print ("Year : ",x.year)
print("day:",x.strftime("%A"))

# CREATING A DATE OBJECTS : TO CREATE A DATE WE CAN USE THE DATETIME() CLASS (CONSTRUCTOR) OF THE DATETIME MODULE . 
# THE datetime () CLASS REQUIRE THREE PARAMETER TO CREATE A DATE : YEAR , MONTH , DAY : 

import datetime
x = datetime.datetime(2005,6,15)
print ("User define : ",x)

# Display the name of month : 
import datetime 
x = datetime.datetime(2025,6,1)
print ("month: ",x.strftime("%B"))