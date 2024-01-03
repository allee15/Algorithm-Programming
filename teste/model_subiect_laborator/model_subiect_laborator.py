#1. a) [0,5p] Scrieți o funcție citire_matrice cu un parametru reprezentând numele unui fișier
#care conține elementele unei matrice de numere întregi cu următoarea structură: pe linia i a
#fișierului sunt elementele de pe linia i a matricei separate printr-un spațiu (vezi exemplul de
#fișier de intrare la punctul c)). Funcția citește elementele matricei din fișierul cu numele dat
#ca parametru și returnează matricea cu aceste elemente. Dacă în fișierul de intrare numărul
#de numere de pe fiecare linie nu este același pentru toate liniile funcția va returna None

#def citire_matrice(fin):
#    l=[]
#    a=[]
#    with open(fin,"r") as f:
#        s=f.read()
#        for x in s.split('\n'):
#            t=[int(y) for y in x.split()]
#            a.append(len(t))
#            l.append(t)
#    for i in range(1,len(a)):
#        if a[0]!=a[i]:
#            return None
#    return l

#b) [1,25p] Scrieți o funcție multimi care primește ca parametri (în această ordine): o
#matrice și un număr variabil de numere naturale reprezentând indici ai liniilor din matrice
#(indicele primei linii din matrice este 0; indicii dați sunt mai mici decât numărul de linii ale
#matricei). Asociem fiecărei linii din matrice două mulțimi: mulțimea elementelor negative de
#pe linie și mulțimea elementelor pozitive care au prima cifră egală cu ultima.
#Funcția returnează următoarele două mulțimi:
#- intersecția mulțimilor elementelor negative asociate liniilor corespunzătoare indicilor dați 
#- reuniunea mulțimilor elementelor pozitive care au prima cifră egală cu ultima asociate
#liniilor corespunzătoare indicilor dați
# (elementele din reuniune sunt distincte două câte două, la fel și cele din intersecție).
#Se acordă jumătate din punctaj dacă în loc de o funcție cu număr variabil de parametri se va
#scrie o funcție multimi  care primește 2 parametri (în această ordine): o matrice și o listă de
#numere naturale reprezentând indici ai liniilor din matrice și returnează informațiile cerute la
#punctul b).
#def verif(x):
#     y=x
#     while y>9:
#        y=y//10
#     if y==x%10:
#         return True
#     else: return False

#def multimi(matrice, *indici):
#         reuniune=set()
#         intersectie=set()
#         nr=0
#         for elem in indici:
#             multneg={}
#             multpoz={}
#             multneg={int(x) for x in matrice[elem] if int(x)<0}
#             multpoz={int(x) for x in matrice[elem] if verif(x)==True}
#             if nr==0:
#                 intersectie =  multneg
#             else:
#                 intersectie = intersectie & multneg
#             reuniune=reuniune | multpoz
#             nr+=1
    
#         return(intersectie,reuniune)

#c) [1,25p] Se dă fișierul "matrice.in" cu structura descrisă la punctul a).  Folosind apeluri utile
#ale funcțiilor de la a) și b) să se citească matricea din fișierul “matrice.in” și să se afișeze pe
#ecran numerele pozitive cu prima cifră egală cu ultima care se află în fișier pe ultimele 3 linii
#(se vor afișa pe aceeași linie, separate prin spațiu, ordonate crescător), precum și numărul de
#elemente negative care se află atât pe prima cât și pe ultima linie din fișier.
#Pentru punctul c) se acordă 1p dacă este rezolvat corect dar fără a folosi funcția de la b).

#l=citire_matrice("matrice.in")
#r=[]
#i=[]
#n=len(l)
#i,r=multimi(l,n-1,n-2,n-3)
#print(*sorted(r,key=None,reverse=False))
#i,r=multimi(l,0,n-1)
#x=len(i)
#print(x)

#2. a) [1p] Scrieți o funcție modifica_prefix cu 3 parametri șiruri de caractere: x, y, prop (în
#această ordine), unde x și y sunt două șiruri diferite de caractere formate doar din litere,
#iar prop este o propoziție în care cuvintele sunt separate prin câte un spațiu. Funcția
#returnează două valori:
#- propoziția obținută modificând propoziția prop astfel: în fiecare cuvânt care începe
#cu x prefixul x este înlocuit cu y
#- numărul de cuvinte al căror prefix a fost modificat 

#def modifica_prefix(x,y,prop):
#    nr=0
#    k=[]
#    for i in prop.split():
#        if i.startswith(x)==True:
#            l=i.replace(x,y)
#            nr=nr+1
#            k.append(l)
#        else:
#            k.append(i)
#    return(k,nr)

#b) [1p] Scrieți o funcție poz_max cu un parametru, care primește ca parametru o listă de
#numere naturale și returnează pozițiile pe care apare maximul în listă (numerotate de la 1)

#def poz_max(l):
#    max=-1
#    k=[]
#    for i in range(1,len(l)):
#        if l[i]>max:
#            max=l[i]
#            k.clear()
#            k.append(i+1)
#        elif l[i]==max:
#            k.append(i)
#    return k
 
#c) [1p] Se dă fișierul "propozitii.in" cu următoarea structură:
#- pe linia k a fișierului se află o propoziție cu cuvintele separate prin câte un spațiu; spunem
#că propoziția de pe linia k are indicele k (cu numerotarea începând de la 1).
#Se citesc de la tastatură două cuvinte diferite a și b (formate doar din litere; cele două cuvinte
#se dau pe o linie, separate prin spațiu). Folosind apeluri utile ale funcțiilor de la a) și b) să se
#rezolve următoarele cerințe:
#- să se creeze un nou fișier "propozitii_modificate.out" cu propozițiile din
#fișierul "propozitii.in" modificate astfel: în fiecare cuvânt care începe cu a prefixul a este
#înlocuit cu b
#- să se afișeze pe ecran indicii k ai propozițiilor în care s-au făcut cele mai multe
#modificări (cu numerotarea începând de la 1), separați prin câte un spațiu.
#Pentru punctul c) se acorda 0,75p dacă este rezolvat corect dar fără a folosi funcțiile de la a)
#și b).

#a,b=input().split()
#p=[]
#fout=open("propozitii_modificate.out","w")
#with open("propozitii.in","r") as fin:
#    s=fin.readline()
#    while s:
#        l=[]
#        nr=0
#        l,nr=modifica_prefix(a,b,s)
#        p.append(nr+1)
#        print(p)
#        for x in l:
#            fout.write(x)
#            fout.write(" ")
#        fout.write('\n')
#        s=fin.readline()
#fout.close()
#print(poz_max(p))

#3. a. [1,25p] Să se memoreze datele din fișier într-o singură structură astfel încât să se
#răspundă cât mai eficient la cerințele b) (ștergerea unei cărți având dat codul cărții și aflarea
#numelui unicului său autor) și c) (accesarea numelui unui autor și a informațiilor despre toate
#cărțile sale, având dat codul autorului).

#b. [0,75p] Să se scrie o funcție sterge_carte cu 2 parametri: în primul parametru se
#transmite structura în care s-au memorat datele la cerința a), iar al doilea este codul unei
#cărți, care șterge din structura de date primită toate informațiile legate de cartea cu codul
#dat ca parametru. Funcția returnează numele unicului autor al cărții cu codul dat,
#sau None dacă acea carte nu s-a găsit.
#Să se apeleze funcția pentru un cod de carte citit de la tastatură și să se afișeze pe
#ecran mesajul “Cartea a fost scrisa de … .”, sau
#mesajul “Cartea nu exista.”. Apoi să se afișeze pe ecran toată structura rămasă după ște
#rgere.

def sterge_carte(ls,cod):
    for key in dict2.keys():
        cheie=int(key)
        if cheie==cod:
            cod_autor=dict2[key][0]
            dict2.pop(key)
            return dict1[cod_autor]
    return None

#c. [1p] Să se scrie o funcție carti_autor cu 2 parametri: în primul parametru se
#transmite structura în care s-au memorat datele la cerința a), iar al doilea este codul
#unui autor. Funcția returnează numele autorului și o listă cu informații despre cărțile sale (un
#element al listei fiind un tuplu ce conține: numele cărții, anul apariției, numărul de pagini),
#lista fiind sortată crescător după anul apariției, în caz de egalitate descrescător după numărul
#de pagini, iar în caz de egalitate crescător după numele cărții. Funcția va returna o listă vidă
#dacă nu există un autor cu codul primit ca parametru.
#Să se apeleze funcția pentru un cod de autor citit de la tastatură și să se afișeze
#rezultatul returnat ca în exemplul de mai jos.
def cheie(lista):
    return lista[1],-lista[2],lista[0]
def carti_autor(ls,cod):
    ver=0
    for item in dict2.values():
        if item[0]==str(cod):
            ver=1
            item=item[1]
            ti=item[2:]
            ti=" ".join(ti)
            an_ap=int(item[0])
            nr_pg=int(item[1])
            tuplu=(ti,an_ap,nr_pg)
            ls_inf.append(tuplu)
        if ver==0:
            return ls_inf
        nume_autor=dict1[str(cod)]
        ls_sorted=sorted(ls_inf,key=cheie)
        return nume_autor,ls_sorted     

ls=[]
dict1={}
dict2={}
with open("autori.in","r") as f:
    linie=f.readline()
    linie=linie.split()
    m= int(linie[0])
    n=int(linie[1])
    for i in range(m):
        linie=f.readline()
        linie=linie.split(maxsplit=1)
        cod_autor=linie[0]
        nume_autor=linie[1].rstrip('\n')
        dict1[cod_autor]=nume_autor
    for i in range(n):
        linie=f.readline()
        linie=linie.split(maxsplit=2)
        cod_autor=linie[0]
        cod_carte=linie[1]
        informatii=linie[2].rstrip('\n')
        informatii=informatii.split()
        val=[]
        val.append(cod_autor)
        val.append(informatii)
        dict2[cod_carte]=val
    ls.append(dict1)
    ls.append(dict2)
    print(ls)

    cod=input("cod=")
    raspuns=sterge_carte(ls,cod)
    if raspuns!=None:
        print(raspuns)
    else: print("nu exista")

ls_inf=[]
rez=carti_autor(ls,11)
if ls_inf==[]:
    print("cod incorect")
else:
   print(rez[0])
   rez=rez[1]
   for i in rez:
       print(*i)

   

