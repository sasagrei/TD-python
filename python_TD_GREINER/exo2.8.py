x = float(input("Entrez un nombre décimal :"))

if ((not x <= 2 and x < 3) or (not x < 0 and x <= 1) or (not x <= -10 and x <= -2)):
    print("x appartient à I")
else: print("x n'appartient pas à I")


#((2 <= x < 3) or (0 < x <= 1) or (-10 <= x <= -2)):