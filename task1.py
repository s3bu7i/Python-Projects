

def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))


def find_max(lst):
    max = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max


lst = [3, 7, 1, 9, 4]
# print(find_max(lst))  # Output: 9

d = {
    "appel": 3,
    "ajhuusd": 5,
    "uyyshsh": 66
}

for key in d:
    if key[0] == "a":
        print(key)

total = 0

for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)
