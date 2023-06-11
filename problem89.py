# to gen even, 0 to 20
# add even
# to gen odd, 0 to 20
# add odd 
# add even + odd
s1 = 0
s2 = 0
for i in range(0,21):
    if (i%2 == 0):
        s1 += i
        print(i)
print("Even number = "+str(s1))

for i in range(0,21):
    if (i%2 != 0):
        s2 += i
        print(i)
print("Odd number = "+str(s2)) 
print("Total result is = "+str(s1+s2))       