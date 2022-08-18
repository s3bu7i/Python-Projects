fakto = int(input("lütfen faktoriyel hesaplanacak sayıyı giriniz:\n"))


def faktohesapla(x):
    sayac = 1
    if x == 0:
        return 1
    else:
        for i in range(1, x+1):
            sayac *= i

        return sayac


sonuc = faktohesapla(fakto)


print(f"verdiğiniz faktoriyelin sonucu: {sonuc}")


# Sorry, I don't know your language so I don't understand variable names. I tweaked your code a bit


