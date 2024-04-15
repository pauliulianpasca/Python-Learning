from Classes import Persoana  # Sau cu * daca vrem sa importam tot

# Obiecte

Mihai = Persoana(30, "masculin")
print(Mihai.varsta)
Mihai.alerg()

Ana = Persoana(28, "f")
print(Ana.sex)
Ana.mananc()

# Tema Obiecte

from Classes import Dog

Bruno = Dog("white", 3, "husky")
print("Color: ", Bruno.color)
print("Age: ", Bruno.color)
print("Breed: ", Bruno.color)
Bruno.run()
Bruno.eat()

Bella = Dog("golden", 4, "Labrador")
print("Color: ", Bella.color)
print("Age: ", Bella.color)
print("Breed: ", Bella.color)
Bella.run()
Bella.eat()