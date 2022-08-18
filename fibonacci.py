

user = int(input("How many fibonacci numbers do you want ?"))
fibonacci_no = [0,1]

while True:
    adding_no = fibonacci_no[-1] + fibonacci_no[-2]
    fibonacci_no.append(adding_no)
    if len(fibonacci_no) == user:
        break
    
for i in fibonacci_no:
    print(i)