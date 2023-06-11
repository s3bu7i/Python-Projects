# to get 10 color
# copy of color list
# Display both list


color_list = []
for i in range(10):
    color_list.append(input("Enter color name"))

print("Orignal List = "+str(color_list))

new_color_list = color_list.copy()
new_color_list.pop()
print("Copied List = "+str(new_color_list))
