# To get bio from the user
# find total char in the bio
# find total word in the bio
# display result

user_bio = input("Enter your Bio")
print("Your bio is \n")
print(user_bio)
print("Total char = "+str(len(user_bio)))

user_bio_list =  user_bio.split()
print("Total words = "+str(len(user_bio_list)))