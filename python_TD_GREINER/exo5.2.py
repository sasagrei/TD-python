moyenne = 0
inf8 = 0

for i in range(5):
    tout = input("Note + coeff : ")
    seg = tout.split(" ")
    note = int(seg[0])
    coeff = int(seg[1])
    moyenne += coeff * note
    if note < 8:
        inf8 += 1

moyenne/5

if moyenne > 10 and inf8 == 0:
    print("Eleve admis !")
else: print("Non-admis !")