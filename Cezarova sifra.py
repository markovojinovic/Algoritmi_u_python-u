print('Unesite poomeraj za sifrovanje Cezarovom sifrom')
pomeraj = int(input())

print('Unesite poruku koju zelite da sifrujete')
poruka = input()
por = list(poruka)

for i in range(len(por)):
    if(por[i] != " "):
        por[i] = chr(((ord(por[i]) - 97 + pomeraj) % 25) + 97)

poruka = "".join(por)
print('Vasa poruka kao sifrovana izgleda ovako:')
print(poruka)

for i in range(len(por)):
    if (por[i] != " "):
        por[i] = chr(ord(por[i]) - pomeraj)
        if(ord(por[i]) < 97):
            por[i] = chr(ord(por[i]) + 25)

poruka = "".join(por)
print('Vasa poruka kao desifrovana izgleda ovako:')
print(poruka)