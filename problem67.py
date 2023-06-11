# to get a num
# positive and less than 50

num1 = int(input("Enter 1st num"))
num2 = int(input("Enter 2nd num"))

if((num1>0 and num2>0) and (num1<50 and num2<50)):
    print("Addition of both numer is "+str(num1+num2))
else:
    print("Number should be positive and less than 50")