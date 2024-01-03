#grupa 144, Aldea Alexia Elena
#Subiectul 3
#Se consideră fișierul text note.in cu următoarea structură:
#• pe prima linie apar, despărțite prin spațiu, numărul n reprezentând 
#numărul de elevi dintr-o 
#clasă a unui liceu și numărul m reprezentând numărul de materii
#• pe următoarele linii avem informații despre n elevi; pentru fiecare elev 
#informația are 
#următoarea structură:
#▪ linie de forma <șir de caractere> reprezentând numele elevului
#▪ urmată de m linii care conțin notele elevului (numere naturale nenule) 
#la m materii, 

resf = open('note.in','r')

n, m = [int(i) for i in resf.readline().split(' ')]

d = {}
for i in range(n):
    nume = resf.readline()[:-1]
    d[nume] = {}
    for j in range(m):
        line = resf.readline().split(',')
        d[nume][line[0]] = [int(nota) for nota in line[1:]]

def medie(note):
    res = 0
    print(note)
    for i in note:
        res+=i
    return round(res/len(note),2)

def despre_elev(d,elev):
    return [(i[0],medie(i[1])) for i in d[elev].items()]

def adauga_nota(d,elev,materie,*args):
    d[elev][materie]+=list(args)

def detect_elev(d):
    stin = input("")
    for name in d:
        if name in stin:
            print(name)
            elems = stin.split(' ')
            adauga_nota(d,name,elems[-3],int(elems[-2]),int(elems[-1]))
            print(elems[-3],medie(d[name][elems[-3]]))

detect_elev(d)
