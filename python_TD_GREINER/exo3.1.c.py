inf10=0
inf15=0
sup15=0
i=0

while i<10:
    a=int(input("Nombre entre 0 et 20 :"))
    if 0<=a<=20:
        if a<10:
            inf10+=1
        else: 
            if a<15:
                inf15+=1
            else: sup15 +=1
        i+=1
    else: print("Entre 0 et 20 svp :")

print("Nombre de valeurs inférieur strictement à 10 : {} \n Nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 : {} \n Nombre de valeurs supérieur ou égale à 15 : {}".format(inf10, inf15, sup15))