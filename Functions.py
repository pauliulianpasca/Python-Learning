#Definirea funtiei

def adunare():
    a = 1 + 1
    print(a)

#Apelarea funtiei
adunare()


# Definire funtie cu parametrii

def scadere(x, y):
    a = x - y
    print(a)

# Apelare functie cu parametrii
scadere(3, 5)
scadere(7, 3)
scadere(100, 40)


# Functii deja definite in Py

print(pow(2,3))    # ridica la putere
print(round(1.6))  # rotunjeste valoarea
print(abs(-5))     # returneaza valoarea absoluta

def sortPar(nr):
    if nr % 2 == 0:
        print(nr)
    else:
        print(nr, "nu e numar par")

sortPar(7)

#Tema functii

def comp(x, y):
    if x == y:
        print("Numerele sunt egale")
    elif x > y:
        print(x,"Este mai mare")
    elif x < y:
        print(y,"Este mai mare")
comp(2, 2)
comp(5, 7)
comp(6, 5)


def lista(orase):
    for x in orase:
        print(x)
orase = ["Constanta", "Arad", "Timisoara"]
lista(orase)
lista(["Iasi", "Cluj", "Bucuresti"])