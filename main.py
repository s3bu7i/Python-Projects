
import uuid
import hashlib

def hash_pass(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest + ":" + salt

def check_pass(hash_password,user_pass):
    password,salt = hash_password.split(':')
    return password == hash.sha256(salt.encode() + user_pass.encode().hexdigest)


new_pass = input("Please enter a password :")
hash_password = hash_pass(new_pass)

print("the string to store in the db is :" + hash_password)

old_pass = input("now please enter the password again to check :")

if check_pass(hash_password,old_pass):
    print("you entered the right password...")
    
else:
    print("passwords to not much...")

    
