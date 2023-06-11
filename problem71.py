# to get a sentence 
# count specefic word or char

s = input("Enter a sentence ")
w_c = input("Enter a char or word, you want to count ")
total_n = s.count(w_c)

print("Your sentence "+"\'"+s+"\'")
print("Your word or char you want to count is "+"\""+w_c+"\"")
print(str(total_n)+" time "+w_c+" is present in a sentence ")