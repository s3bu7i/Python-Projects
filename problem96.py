# to get 10 data items from user
# find int, float and string

lst = [1,3.3,'faisal','34','32',5.2,'age', 4,2,54]
integer = 0
float_type = 0
str_type = 0
for i in lst:
    if(type(i) == int):
        integer += 1
    if(type(i) == float):
        float_type += 1
    if(type(i) == str):
        str_type += 1
print("Integer Data type = "+str(integer))
print("Floating Data Type = "+str(float_type))
print("String Data type = "+str(str_type))