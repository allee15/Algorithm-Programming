def cheieSortare(l):
     return l[2] / l[1]


 f = open("rucsac.in")
 G = float(f.readline())
 obiecte = []
 crt = 1
 for linie in f:
     aux = linie.split()
     obiecte.append((crt, float(aux[0]), float(aux[1])))
     crt += 1
 f.close()
 obiecte.sort(key=cheieSortare, reverse=True)
 n = len(obiecte)
 spatiu_liber = G
 solutie = [0] * n
 for i in range(n):
     if obiecte[i][1] <= spatiu_liber:
         spatiu_liber -= obiecte[i][1]
         solutie[i] = 1
     else:
         solutie[i] = spatiu_liber / obiecte[i][1]
         break

 castig = sum([solutie[i] * obiecte[i][2] for i in range(n)])
 g = open("rucsac.out", "w")
 g.write("Castig maxim:" + str(castig)+"\n")
 g.write("Obiectele incarcate:\n")
 i=0
 while i<n and solutie[i]!=0:
     procent=format(solutie[i]*100,'.2f')
     g.write("Obiect"+ str(obiecte[i][0])+":"+ procent+"%\n")
     i+=1

 g.close()
