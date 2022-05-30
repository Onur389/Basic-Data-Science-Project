from asyncio.streams import FlowControlMixin
from re import S
import numpy as np
from matplotlib import pyplot as plt



# Regression and Classification are used in machine learning. 

# If we are trying to estimate variables in our model,that is regression.

# If we are trying to estimate categorical things in our model, that is classification.



# Firstly, i will make a function that takes house data and gives us it's Price.

def estimatePrice(size = 0,bathnumber = 0,roomnumber=0,balconynumber= 0,floornumber =0,saloonnumber =0):
    dolarsperitems = {"size": 750,"bathnumber":1000,"roomnumber":2000,"floornumber":5000,"balconynumber":1000,"saloonnumber":1200}
    
    housevalue = size*dolarsperitems["size"] + dolarsperitems["bathnumber"]*bathnumber + dolarsperitems["roomnumber"]*roomnumber+dolarsperitems["floornumber"]*floornumber+dolarsperitems["balconynumber"]*balconynumber+dolarsperitems["saloonnumber"]*saloonnumber
    return str(housevalue) + "$"

print("\n"*5)
# Let's say we have a house that is 300 metersquare and has 1 bath 1 saloon 1 floor 1 balcony and 2 rooms

# The value of the house is;

print("The value of the house:" + estimatePrice(300,1,2,1,1,1))


# Secondly, i will make a function that takes day names and returns if it's rest day or not
print("\n"*5)

def estimateDay(dayname):
    try:
        dayname = dayname.capitalize()
    except:
        print("Please enter string")
    
    
    days = {"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":1,"Sunday":1}


    if days[dayname]:
        return "{} is a rest day".format(dayname)
    else:
        return "{} is not a rest day".format(dayname)

# Let's see if monday is a rest day;

print(estimateDay("monday"))


# DATA TYPES
# We are classifying data as 4 categories. 
# Numerical (ratio,interval). 
# We use interval data when there's no reference point. for example temperatures. There is no absolute zero in temperatures.
# We use ratio data when there's reference point. It means there is absolute zero. for instance number of personals in bakery.
# Categorical (binary,multiclass).
# Binary is a categorical data when we have only two category in our model.
# When we have more than 2 category in our model, we say can tell is a multiclass data.
# We can also seperate categorical data as Nominal, Ordinal and Cardinal.
# If we can put our data in order like first house and second house, it is nominal data.
# If we say something's features, its ordinal data.
# If we say just a number of somethings like there's 2 houses. It's cardinal data
