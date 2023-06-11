# To get terms
# to get value of that terms
# total/terms
term = int(input("Enter total terms")) # 4
lst = []
for i in range(term):
    lst.append(int(input("Enter terms values")))
#print(lst)
s = 0
for v in lst:
    s += v
print("You entered "+str(term)+" terms")
print("Total of terms values is "+str(s))
print("Average is equal to "+str(s/term))
