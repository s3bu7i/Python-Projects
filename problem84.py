# to get name
# convert to uppercase if not
# display to user

name = input("Enter your name")

if(name.isupper()):
    print("Name is already in uppercase "+name)
else:
    print("Lowercase name is converted to uppercase that is "+name.upper())