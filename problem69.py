# create file
# get name and age 
# write on the file

file = open("jafri.txt","w+")
name = input("Enter your name")
age = input("Enter your age")
file.write("Your name is "+str(name))
file.write("Your age is "+str(age))
file.close()
