nb = int(input("Votre nombre :"))

tot = 0
tot = nb

b100 = nb//100
print(b100)
nb -= 100*b100
print(nb)
b50 = nb//50
nb -= 50*b50
b10 = nb//10
nb -= 10*b10
p2 = nb//2
nb -= 2*p2
p1 = nb//1

print("{} euros, c’est donc {} billets de 100, {} de 50, {} de 10, {} pièces de 2 et {} pièces 1.".format(tot, b100, b50, b10, p2, p1))