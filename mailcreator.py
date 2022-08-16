

def mailcreate(nickname,mailtype="gmail.com"):
    mailadresi="@".join([nickname,mailtype])
    return mailadresi

nickname=input("Enter the nickname : ")
mail=input("Enter the mail : ")
if mail:
    print("mail adress: ", mailcreate(nickname, mail))
else:
    print("mail adress : ",mailcreate(nickname))

