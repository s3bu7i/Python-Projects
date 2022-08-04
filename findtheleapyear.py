

year = int(input("Give a year :"))

if year%4==0:
    if year%100==0:
        if year%400==0:
             print("It is a leap year.")
        else:
            print("Not leap year.")
    else:
        print("It is a leap year.")
else:
    print("Not leap year.")





