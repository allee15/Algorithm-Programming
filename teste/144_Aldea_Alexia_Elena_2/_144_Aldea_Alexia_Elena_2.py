#grupa 144, Aldea Alexia Elena
#Subiectul 2
#a) [0,5p] Fișierul "date.in" conține n>1 linii cu următoarea structură:
# pe linia i se găsesc n 
#numere naturale nenule separate prin câte un spațiu. Să se scrie o funcție
# citire care să 
#citească datele din fișier și să returneze matricea de dimensiuni 𝑛 × 𝑛 care 
#conține numerele 
#în ordinea din fișier.
#b) [1,5p] Să se scrie o funcție modifica_matr care primește ca parametri o
# matrice pătratică 
#𝑛 × 𝑛 și un număr variabil de parametri 𝑥1, 𝑥2, . . . 𝑥𝑘 cu valori cuprinse
# între 0 și n-1, 
#reprezentând indicii unor linii/coloane. Funcția va modifica matricea primită 
#ca parametru 
#astfel:

def citire(fin):
    l=[]
    with open(fin,"r") as f:
        s=f.read()
        for x in s.split('\n'):
            t=[int(y) for y in x.split()]
            l.append(t)
    return l

def modifica_matr(matr,*args):
    last = []
    for i in range(len(matr)):
        if i in args:
            s=0
            for j in range(len(matr)):
                s+=matr[j][i]
            last.append(s)
        else:
            last.append(-1)
    matr.append(last)
    for i in range(len(matr)):
        if i in args:
            mx=-1000
            for j in range(i,len(matr[0])):
                mx = max(mx,matr[j][i])
            matr[i].insert(0,mx)
        else:
            matr[i].insert(0,-1)
    return matr

l=citire("date.in")
print(l)
n = len(l)
if n%2==0:
    indexes = (0,1,n//2,n//2+1,n-1)
else:
    indexes = (0,1,n//2+1,n-1)
l = modifica_matr(l,*indexes)

fmt = '%4d '*len(l[0])
for line in l:
    print(fmt%tuple(line))
