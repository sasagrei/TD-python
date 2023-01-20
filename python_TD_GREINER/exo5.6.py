import random as rdm
import string

size=0
voy = 0
rdmi=rdm.randint(1, 94)
T=[]
V=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for i in range(rdmi):
    T.append(''.join(rdm.choice(string.ascii_letters)))

T.append('w')
T.append('a')
T.append('g')
T.append('o')
T.append('n')

T.append(0)
print(T)


"""
T = ''.join(rdm.choices(string.ascii_letters, k = rdmi)) + '0'
print(T)
"""
debut = -1
wagon = 0

for j in range(99):
    if T[j] == 0:
        break

    """for k in range(10):
        if (T[j] ==  V[k]):
            voy += 1
        """
    if T[j] in V:
        voy += 1

    
    if T[j] == 'w':
        if T[j+1] == 'a' and T[j+1] != 0 :
            if T[j+2] == 'g' and T[j+2] != 0:
                if T[j+3] == 'o' and T[j+2] != 0 :
                    if T[j+4] == 'n' and T[j+2] != 0 :
                        if debut == -1:
                            debut = j
                        wagon += 1  

            

    size += 1

per_voy = round(voy*100/size)

print(size)
print(voy, per_voy, "%")
print(debut, wagon)