# create list
# store num
# display only number that div by 3

#num_list = [2,3,4,5,6,7,12,15,9,43,24,1325,541]
num_list = []
for i in range(10):
    num_list.append(int(input("Enter list item")))
   
for i in num_list:
    if(i%3==0):
        print(i)
