from datetime import datetime
val = input("Do you want to get date and time? yes or no ")

def display_date(v):
    if(v == "yes"):
        print(datetime.now())
    elif(v == "no") :
        print("Okay, we did not display date")
    else:
        print("Please enter value yes or no")     
display_date(val)