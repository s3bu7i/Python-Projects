# to create a list
# store element 
# find middle 

lst = [4,5,1,4,2]
l = len(lst)
print("Length of list = "+str(l))
print("Items of List")
for i in lst:
    print(i)

half = l/2
middle_el = int(half)
#print(middle_el) # 3
print("Middle Element = "+str(lst[middle_el]))