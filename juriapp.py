
from typing import Counter


juripointlist = []
def juriquestion():

    Counter = 1
    while Counter < 6:

        juripoint = int(input(" {}. juri enter the point : ".format(Counter)))
        juripointlist.append(juripoint)
        Counter += 1

def avaragesum(defaultliste):

    top = 0
    workmannum = len(defaultliste)
    for i in juripointlist:
        top = i + top
    return top / workmannum






def comment():
    if avarage >= 3.5 and avarage <= 5:
        print("You didn't pass, try some more ")


    elif avarage >=1 and avarage <=3 :
        print("The jury never liked you :)")

    elif avarage > 5 and avarage <=7:
        print("You passed, good luck...")

    elif avarage > 7 and avarage <=9:
        print("You were amazing, the jury was amazed","your avarage : {}".format(avarage))



juriquestion()
avarage=avaragesum(juripointlist)
print(comment())