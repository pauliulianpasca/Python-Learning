# IF Statement (verificam conditii)

a = 2
b = 3

"""
if a > b:
    print("a este mai mare decat b")
elif a < b:
    print("a este mai mic decat b")
else:
    print("a este egal cu b")
"""

# FOR Statement (iterator)

cars = ["audi", "bmw", "dacia"]
for x in cars:
    print(x)

numere = [1, 2, 3]
for x in numere:
    x = x * 10
    print(x)

numere2 = [1, 2, 3]
for x in numere2:
    if x == 2:
        x = x * 10
        print("numere2 =", x)

# Tema - if/for

udemyA = "udemy"
udemyB = "udemy"

if udemyA == udemyB:
    print("Valorile sunt egale")
else:
    print("Valorile nu sunt egale")

numeCaini = ["Bruno", "Daisy", "jack"]
for x in numeCaini:
    print(x)
print(numeCaini[1])