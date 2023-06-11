"""
1 day = 24H
One year = 365 * 24 = 8760H
IH = 3600s
8760H into s?
8760 * 3600 = 31536000s
"""

age = float(input("Enter your age to convert to sec")) 
age_int_s = age * 31536000  
print("Your age is "+str(age))
print("Your age in seconds is "+str(age_int_s))
