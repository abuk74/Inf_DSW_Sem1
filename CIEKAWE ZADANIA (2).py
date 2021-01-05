'''wiek = int(input("ile masz lat?"))
if wiek <= 18:
    print("niepełnoletni")
elif wiek == 100:
    print("masz 100 lat!")
else:
    print("pełnoletni")
'''
import random
'''lista = []
for i in range(0, 6):
    x = random.randint(1, 49)
    print(x)
    y = str(x)
    lista.extend(y)
print(lista)

Numbers=list(range(1,49))
random.shuffle(Numbers)
six_nums=Numbers[:6]
print(six_nums)

a = float(input("Podaj pierwszą liczbe: "))
b = float(input("Podaj pierwszą liczbe: "))

suma = a + b
roznica = a - b
iloczyn = a * b
if b != 0:
    iloraz = a / b

print("Suma: ", suma)
print("Roznica: ", roznica)
print("Iloczyn: ", iloczyn)
print("Iloraz: ", iloraz)



liczby = {1, 69, 666, 10000}
for x in liczby:
    mod = x % 2
    print(mod)

var = sys.maxsize

godzina = 3600
doba = 24 * godzina
rok = 365 * doba + 6 * godzina
zycie = 19 * rok

print(godzina, doba, rok, zycie, "[s]")


km = 30 * 1000
t1 = 15 * 60
t2 = 12 * 60

v1 = km / t1
v2 = 2*km / (t1 + t2)
v3 = v2 * 3600 / 1000
print("srednia predkosc na pierwszym odcinku drogi [m/s]: ", v1)
print("srednia predkosc [m/s]: ", v2)
print("srednia predkosc [km/h]: ", v3)

a = int(input("podaj pierwsza liczbe"))
b = int(input("podaj druga liczbe"))
z = (a / b)
if b != 0:
    if int(z) == a / b:
        print("{} jest podzielne przez {}".format(a, b))
    else:
        print("{} nie jest podzielne przez {}".format(a, b))
else:
    print("nie ma dzielenia przez zero!")


num = input("Podaj liczbe")
if num <= 10:
    print("liczba {} jest mniejsza lub równa 10".format(num))
elif num <= 25:
    print(" liczba {} jest większa od 10, ale mniejsza lub równa 25".format(num))
else:
    print("liczba {} jest wieksza od 25")

from statistics import median
a = input("Podaj pierwsza liczbe")
b = input("Podaj druga liczbe")
c = input("Podaj trzecia liczbe")


lista = {a,b,c}
maxLiczba = max(lista)
mediana = median(lista)
minLiczba = min(lista)
print(minLiczba, mediana, maxLiczba) #tutaj coś nie działa ### bo input na int trzeba przekonwertować


num = int(input("podaj liczbe"))
if num > 0:
    if (num % 2) == 0:
        print("ta liczba dodatnia dzieli sie przez 2 bez reszty")
    else:
        print("ta liczba dodatnia dzieli sie przez 2 z resztą {}".format(num%2))
elif num == 0:
    print("Zero jest nie ujemne i zawsze dzieli sie bez reszty")
else:
    if (num%2) == 0:
        print("ta liczba ujemna dzieli sie przez 2 bez reszty")
    else:
        print("ta liczba ujemna dzieli sie przez 2 z resztą {}".format(num%2))

from statistics import median





a = float(input("Podaj pierwsza liczbe"))
b = float(input("Podaj druga liczbe"))
c = float(input("Podaj trzecia liczbe"))
d = float(input("Podaj czwarta liczbe"))
lista = [a,b,c,d]
maxLiczba = max(lista)
lista.remove(maxLiczba)
minLiczba = min(lista)
lista.remove(minLiczba)
drugaLiczba = lista[0]
trzeciaLiczba = lista[1]
if (drugaLiczba == trzeciaLiczba):
    print(minLiczba, drugaLiczba, trzeciaLiczba, maxLiczba)
elif drugaLiczba < trzeciaLiczba:
    print(minLiczba, drugaLiczba, trzeciaLiczba, maxLiczba)
else:
    print(minLiczba, trzeciaLiczba, drugaLiczba, maxLiczba)


import math
a = float(input("podaj wspolczynnik a"))
b = float(input("podaj wspolczynnik b"))
c = float(input("podaj wspolczynnik c"))
x = float(input("podaj zmienna x"))
if a != 0:
    print(" y = ", (a * x**2 + b * x + c))
    delta = (b**2 - 4 * a * c)
    if delta > 0:
        x1 = -b - math.sqrt(delta)/(2 * a)
        x2 = -b + math.sqrt(delta)/(2 * a)
        print("miejsca zerowe tej funkcji:", str(x1), str(x2))
    elif delta == 0:
        x1 = -b / (2 * a)
        print("pierwiastek tej funkcji wynosi: ", str(x1))
    else:
        print("brak miejsc zerowych")
else:
    print("To nie jest trojmian kwadratowy!")

'''
