# to get 10 std marks
# store in list, 
# find 2nd position

std_marks = [] # 2,4,5,6,7

for i in range(10):
    std_marks.append(int(input("Enter student marks")))
std_marks.sort(reverse=True)
print("Total Result of Students = "+str(std_marks))
print("2nd Student Marks = "+str(std_marks[1]))