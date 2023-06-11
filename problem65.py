# to get lenght of square

l = float(input("Enter lenght of square"))

def area_peri(lenght):
    area = lenght*lenght
    perimeter = 4*lenght
    print("Area = "+str(area))
    print("Perimeter = "+str(perimeter))
area_peri(l)