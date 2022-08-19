

import time
import random
word_list = ["school","car","book"]

word = random.choice(word_list)
#print(word[0])

word_length = len(word)
#print(word_length)

dash_list = []
for letter in word:
    dash_list.append("-")

print(dash_list)

life=8
while True:
    guess = input("Type a letter :")
    
    if guess in word:
        b=0
        for letter in word:
            
            if guess == letter:
                dash_list[b] = guess
                
            else:
                pass
            b+=1   
        print(dash_list)   
         
    else:
        print(dash_list)
        life-=1
        print("False")
        print(f"Your have {life} lives")
        
    if life==0:
        print("You lost :(")
        break
    
    if "-" not in dash_list:
        print("You won :)")
        break
time.sleep
