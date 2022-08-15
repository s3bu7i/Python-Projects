





fakto=int(input("lütfen faktoriyel hesaplanacak sayıyı giriniz : "))





def faktohesapla(x):
    sayac=1
    if x == 0 :

        return 1

    else:
        for i in range(1,x+1):
            sayac=sayac*i

        print("{} sayısının faktoriyeli : ".format(x),sayac)

sonuc=faktohesapla(fakto)


print("verdiğiniz faktoriyelin sonucu ",sonuc)





