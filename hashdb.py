

import hashlib

veri=input("Enter the data to be encrypted : ")


hashing=hashlib.sha256()
hashing.update(veri.encode("utf-8"))

#5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5
print(hashing.hexdigest())




