def indexNiza(karakter, niz):
    for i in range(len(niz)):
        if(niz[i] == karakter):
            return i

    return -1


print('Unesite kljuc')
k = input()

while(len(k) < 26):
    k = k + k

k = k[:26]
kljuc = list(k)

print('Unesite poruku koja treba da se sifruje')
p = input()
poruka = list(p)

for i in range(len(poruka)):
    if(poruka[i] != " "):
        poruka[i] = kljuc[ord(poruka[i]) - 97]

p = "".join(poruka)
print('Sifrovana poruka izgleda ovako')
print(p)

for i in range(len(poruka)):
    if(poruka[i] != " "):
        poruka[i] = chr(indexNiza(poruka[i], kljuc) + 97)

p = "".join(poruka)
print('Desifrovana poruka izgleda ovako')
print(p)

#napadamo u podne ako ne bude vetra

#qwertzuiopasdfghjklyxcvbnm