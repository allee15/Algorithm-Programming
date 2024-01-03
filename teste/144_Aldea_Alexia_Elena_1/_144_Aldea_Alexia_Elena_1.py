#grupa 144, Aldea Alexia Elena
#Subiect 1
#[4 p.] Fișierul text numere.in conține, pe fiecare linie, câte un șir de
# numere întregi despărțite 
#prin spații. Să se scrie în fișierul text numere.out șirurile din fișierul 
#de intrare grupate în 
#funcție de suma elementelor lor, conform modelului din exemplul de mai jos.
# Grupele de 
#șiruri vor fi scrise în ordinea crescătoare a sumelor elementelor lor, iar 
#în fiecare grupă șirurile 
#se vor scrie în ordinea descrescătoare a numărului de elemente. 
def suma(l):
    suma=0
    for x in range(len(l)):
        suma=suma+l[x]
    return suma

d={}
with open("numere.in","r") as fin:
    lines=fin.readlines()
    for s in lines:
        x = [int(i) for i in s.split()]
        sumal=suma(x)
        if sumal not in d:
            d[sumal]= [x]
        else:
            d[sumal].append(x)

lst = list(d.items())
lst.sort()
d = dict(lst)
with open('numere.out','w') as out:
    for suma in d:
        out.write('Suma %d:\n'%suma)
        for line in d[suma]:
            buf = ''
            for w in line:
                buf += str(w)+' '
            out.write(buf+'\n')
    out.close()
