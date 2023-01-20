cat = input("palindrome ? ")

def remove_at(i, s):
    return s[:i] + s[i+1:]


cat1=""
for i in range(len(cat)):
    if cat[i].isalpha():
        cat1 += cat[i]
print(cat1)

pal = 0
print(len(cat1))
a = 0

for j in range(len(cat1)):
    if cat1[j] != cat1[(len(cat1)-1-a)]:
        print("pas un palindrome")
        break
    else: 
        pal+=1
    a+=1

if pal == len(cat1):
    print("palindrome")


""" for j in range(len(cat)):
            if j != i:
                cat1 = cat1 + cat[j]
        cat = cat1
        print(cat)
        i-=1
    if i == len(cat) or i > len(cat):
        break
    """





