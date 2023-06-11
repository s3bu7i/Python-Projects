# to create a list
# insert std name
# display all the std name except f char started name

std_list = ['ali','kami','faisal','faiz','yash']
print(std_list)
for i in std_list:
    if(not(i.startswith('f'))):
        print(i)