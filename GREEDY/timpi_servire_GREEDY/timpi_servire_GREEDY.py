 def sortare(t):
     return t[1]


 def afisare(ts):
     nr_tot = 0
     nr_crt = 0
     for i in ts:
         nr_crt = nr_crt + int(i[1])
         nr_tot = nr_tot + nr_crt
         print(str(i[0]).center(len("Persoana")),
               str(i[1]).center(len("Timp de servire")),
               str(nr_crt).center(len("Timp de asteptare")), sep="\t")
         print("Timpul mediu de asteptare:", round(nr_tot / len(ts), 2))


 timpi_serv = [x for x in input("Timpii de servire sunt:").split()]
 pers = [(i + 1, timpi_serv[i]) for i in range(len(timpi_serv))]
 afisare(pers)
 pers.sort(key=sortare)
 afisare(pers)
 def sortare(l):
     return l[2]
 fin=open("spectacole.txt")
 lsp=[]
 crt=1
 for linie in fin:
     aux=linie.split("-")
     lsp.append((crt, aux[0].strip(),aux[1].strip()))
     crt=crt+1
 fin.close()
 lsp.sort(key=sortare)
 l=[]
 l.append(lsp[0])
 for sp in lsp[1:]:
     if sp[1]>l[len(l)-1][2]:
         l.append(sp)
