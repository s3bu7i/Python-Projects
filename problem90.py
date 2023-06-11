# to get 10 std age
# store in list
# dispaly age greater than 14 and less than 20

std_age = []

for i in range(0,10):
    std_age.append(int(input("Enter Age of student")))

for i in std_age:
    if(i > 14 and i < 20):
        print(i)
