import random

#======================Mozda ima nekih gresaka, nije potpuno sigurno
def stepenDvojke(broj):
    br = int(broj) - 1
    k = 0
    while(1):
        if(br / 2 >= 1 and br / pow(2,k) % 2 != 1):
            k = k + 1
            br = br / 2
        else:
            break
    return k + 1

def mnozilacZaStepen(broj, stepen):
    return (broj - 1) / pow(2, stepen)

def MilerRabinovAlogritam(broj, stepen, mnozilac):
    slucajan = random.randint(1, broj - 1)

    if (pow(slucajan, mnozilac) % broj == 1):
        return True
    else:
        for j in range(stepen):
            if (pow(slucajan, pow(2, j) * mnozilac) % broj == broj - 1):
                return True
    return False

print('Unesite prost broj veci od 2')
broj = int(input())

stepen = stepenDvojke(broj)
mnozilac = mnozilacZaStepen(broj, stepen)

k = 0
for j in range(50):
    if(MilerRabinovAlogritam(broj, stepen, mnozilac)):
        k = k + 1
    else:
        k = k - 1

if(k < 12):
    print('Mozda nije prost')
else:
    print('Mozda je prost')