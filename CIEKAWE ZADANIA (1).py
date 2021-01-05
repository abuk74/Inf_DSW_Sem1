'''
def Hello():
    print("Hellow world!")
    return
#Hello()
def Silnia(n):
    if n > 1:
        return n * Silnia(n-1)
    else:
        return
    return
#Silnia(3)

i = 0
while i != 100:
    print(i, "to jest efekt petli while")
    i +=1

i = 1
while i != 21:
    if (i % 2 == 0 or i % 3 == 0):
        i +=1
    else:
        print(i)
        i +=1

i = 0
while i != 6:
    i +=1
    if i != 2:
        print(i)
    else:
        continue

while True:
    var = float(input("Podaj liczbe"))
    if var % 69 == 0:
        print("Liczba podzielna przez 69")
        break;

newNum = 0
while True:
    num = float(input("Podaj liczbe"))
    newNum += num
    if newNum > 100:
        print(newNum, "jest wieksze od 100 wiec koncze dzialanie petli")
        break;

i = float(input("Podaj liczbe"))
while True:
    if int(i) == 0:
        break
    else:
        print(int(i))
        i -= 1

k = 0
srednia = 0
while True:
    try:
        num = float(input("Podaj wartość"))
        if num != 0:
            srednia += num
            k += 1
        else:
            print("trafilem na 0, koncze dzialanie programu")
            print(srednia/k)
            break
    except ValueError:
        break

num = float(input("Podaja liczbe"))
i = 0
suma = 0
while num % 2 == 0 or num % 3 == 0:
    i += 1
    if num % i == 0:
        if i == num:
            break
        suma += i
        print(suma)
    else:
        if i == num:
            break
        continue

prevnum = 0
num = 0
suma = 0
k = 0
#lista = [1, 5, 8, 12, 24, 66, 69, 69, 18]
lista = []
while True:
    num = float(input("Podaj liczbe"))
    lista.append(num)
    if k == 0:
        num = lista[0]
        prevnum = num
        suma = num
        print(suma)
        k += 1
    else:
        num = lista[k]
        if num != prevnum:
            prevnum = num
            suma += num
            print(suma)
            k += 1
        else:
            break;

for i in range(1,100):
    if i % 8 == 0:
        print(i)

try:
    num = int(input("Podaj liczbe dodatnia"))
    if num > 0:
        for i in range(num, 0, -1):
            if (i % 6 == 0) & (i % 9 == 0):
                print(i)
    else:
        print("Czytanie ze zrozumieniem się kłania")
except ValueError:
    print("To nie jeste liczba")

z3 = []
z4 = []
for i in range(100, 200):
    if (i % 2 != 0) & (i % 3 != 0):
        z3.append(i)
    if (i % 2 == 0) & (i % 3 != 5) & (i % 6 != 0) & (i % 11 != 0):
        z4.append(i)
print("Wynik zadania 3: " + str(z3))
print("Wynik zadania 4: " + str(z4))

sumaS = 0
liczby = 0
for i in range(0,101):
    sumaS += i**3
    if sumaS > 10**6:
        liczby = i
    else:
        continue
print("Potrzebna ilość liczb naturalnych: ", liczby)
print("Suma szeescianow ", sumaS)

from statistics import median
n = int(input("Podaj liczbe"))
x = int(input("Podaj liczbe"))
k = 0
srednia = 0
lista = []
for i in range(n, x+1):
    lista.append(i)
    srednia += i
    if k !=6:
       k +=1
       print(i)
    else:
        continue
    if i == x+1:
        break
print(median(lista))
print(srednia/len(lista))
print(min(lista))
print(max(lista))

import random
import time
currentTime = time.time()
num = random.randint(1, 100)
for i in range(0,4):
    if i <3:
        x = int(input("Zgaduj liczbe"))
        if x > num:
            print("podałeś za duza wartosc")
        elif x < num:
            print("podalesz za mala wartosc")
        else:
            print("Zgadles!")
            break
    else:
        print("Haha przegrales!")
print(time.time() - currentTime)


import random

randomList = random.sample(range(0,50), 10)
print("Lista przed zmieszaniem: ", randomList)
random.shuffle(randomList)
print("Pomieszana lista: ", randomList)
randomList.sort(reverse = False)
print("Posortowana lista:", randomList)


n = int(input("Podaj liczbe"))
a, b = 0, 1
print("wyraz", 1, a)
print("wyraz", 2, b)
for i in range(1, n - 1):
    a, b = b, a + b
    print("wyraz", i + 2, b)

tup = (1,2,3,4,5,6)
print(tup)
print(id(tup))
tup2 = tup + (7,8)
print(tup2)
print(id(tup2))
lista = list(tup2)
print(lista)
print(id(lista))

import random
lista = []
num0 = 0
num1 = 0
for i in range(0,100):
    num = random.randint(0, 10)
    lista.append(num)
    if num == 0:
        num0 +=1
    elif num == 1:
        num1 += 1
tup = tuple(lista)
print(tup)
print(num0)
print(num1)


import webbrowser

url = "https://devillecloud.com/"
db = {
    "Gandalf" : '123',
    "admin" : 'admin',
    "Geralt" : '123',
    "Ciri" : '321',
    "Johnny" : '123',
    "V" : '321'
}
while True:
    login = input("Login: ")
    password = input("Password: ")
    if password == db.get(login):
        if 'admin' != db.get(login):
            print("Logged in as a user ")
            webbrowser.open(url)
            break;
        else:
            print("Logged in as an admin ")
            webbrowser.open(url)
            break;
    else:
        print("incorrect password or login")

import random

list = [43058, 43041, 43044, 43050, 43171, 43047, 43051, 43038, 43169, 43034, 43055, 43056, 43407, 43166]
person = list[random.randint(0, len(list) -1)]
print(person)


import math
a = float(input("Podaj długość pierwszej ściany (w metrach): "))
b = float(input("Podaj długość drugiej ściany: (w metrach)"))
c = float(input("Podaj wysokość (mierzona od podłogi do sufitu, w metrach): "))
okno = 1.1 * 1.4
drzwi = 0.89 * 2

v = a*b*c
pc = (2*(a*b))+(2*(a*c))+(2*(b*c))

print("Twój pokój ma: ", v, "m^3, lub: ", pc, "m^2")

ileokna = int(input("Podaj ile masz okien w pokoju: "))
iledrzwi = int(input("Podaj ile masz drzwi w pokoju: "))

pc2 = ((2*(a*b))+(2*(a*c))+(2*(b*c)))-((okno*ileokna)+(drzwi*iledrzwi))

print("Po poprawkach twój pokój ma powierzchnię: ", pc2, "m^2")

import math

fahrenheit = int(input("Podaj temperaturę w stopniach Fahrenheit'a: "))
celsjusz = (fahrenheit - 32) / 1.8
if celsjusz <= 0:
    print("woda zamarza")
elif celsjusz > 0 and celsjusz < 100:
    print("woda w stanie ciekłym")
else:
    print("woda wrze")

import math

def Main():
    namesOfDef = list(input("Wybierz jednostke wejściową oraz wyjściową: C - Celsjusz, K - Kelwin, F - Fahrenheit"))
    value = int(input("podaj wartość temperatury"))
    if namesOfDef[0] == "K":
        Kelwin(value, namesOfDef)
    elif namesOfDef[0] == "F":
        Fahrenheit(value, namesOfDef)
    else:
        Celsjusz(value, namesOfDef)



def Kelwin(value, namesOfDef):
    if namesOfDef[1] == "C":
        print(value + 273)
    else:
        print(value - 255)


def Fahrenheit(value, namesOfDef):
    if namesOfDef[1] == "C":
        print(value - 32)
    else:
        print(value + 255)


def Celsjusz(value, namesOfDef):
    if namesOfDef[1] == "K":
        print(value - 273)
    else:
        print(value + 32)

Main()
'''
n = int(input("Podaj inta"))
while n != 1:
    if (n-1) % 2 == 0:
        n = n // 2
    else:
        n = 2 * n + 1
    print(n)
