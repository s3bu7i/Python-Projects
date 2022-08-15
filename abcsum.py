

class strtools:

    def __init__(self,word):
        self.sayac = {"harf": 0,
                 "sayı": 0,
                 "büyük": 0,
                 "küçük": 0}

        self.word=word

    def harfsayibul(self):


        for i in self.word:
            if i.isnumeric() == True:
                self.sayac["sayı"] += 1


            elif i.isalpha() == True:
                self.sayac["harf"] += 1

            else:
                pass
        print("{} string ifadesinde".format(self.word))
        print("{} adet harf var".format(self.sayac["harf"]))
        print("{} adet sayı var".format(self.sayac["sayı"]))


    def bigorsmall(self):


        for i in self.word:
            if i.islower() == True:
                self.sayac["küçük"] += 1


            elif i.isupper() == True:
                self.sayac["büyük"] += 1

            else:
                pass
        print("{} adet büyük harf var".format(self.sayac["büyük"]))
        print("{} adet küçük harf var".format(self.sayac["küçük"]))

