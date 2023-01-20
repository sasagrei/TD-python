print("Veuillez saisir une date valide:")
date = input()

if len(date)<8:
    print("Non valide !")

else :
    jour = int(date[0])*10 + int(date[1])
    mois = int(date[2])*10 + int(date[3])
    an = int(date[4])*1000 + int(date[5])*100 + int(date[6])*10 + int(date[7])

    if mois < 1 or mois > 12:
        print("Non valide !")
    else:
        if mois == (1, 3, 5, 7, 8, 10, 12):
            if jour < 0 or jour > 31:
                print("Non valide !")
            else: print("Valide !")
        else:
            if mois == 2:
                if (an%400 == 0) or (an%4 == 0 and an%100 != 0):
                    if jour > 29:
                        print("Non valide !")
                    else: print("Valide !")
                else:
                    if jour > 28:
                        print("Non valide !")
                    else: print("Valide !")
            else:
                if jour < 0 or jour > 30:
                    print("Non valide !")
                else: print("Valide !")
    
        