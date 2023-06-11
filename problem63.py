# To ge 10 number, store in the list
# Pass to function
# find max number
lst = []

for i in range(10):
    lst.append(int(input("Enter number")))
#print(lst)

def max_num(l):
    #print(type(l))
    print(max(l))
max_num(lst)