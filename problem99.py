# to get 10  words from user
# uppercase

lst = []
for i in range(10): # 0 to 9
    w = input("Enter word to store in list")
    if(w.isupper()):
        lst.append(w)
    else:
        print("Error! Insert Uppercase word")
print(lst)
