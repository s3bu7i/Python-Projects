# to get color code
# shuffle the color code and display
import random
color_code = []

for i in range(5):
    color_code.append(input("Enter Color Code"))
random.shuffle(color_code)
print(color_code)
