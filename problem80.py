# to get sentence
# display char of odd index number

s = input("Enter a sentence")
s_len = len(s)
#print(s_len)
for n in range(1,s_len):
    if(n%2!=0):
        print(s[n])
