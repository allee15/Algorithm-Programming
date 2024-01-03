 fout=open("programare.txt",'w')
 fout.write("Numarul maxim de spectacole:"+str(len(l))+"\n")
 fout.write("\nSpectacole programate:\n")
 for sp in l:
     fout.write(sp[1]+"-"+sp[2]+" Spectacol "+str(sp[0])+"\n")
 fout.close()
# #Programare spectacole(mai multe sali)
 import queue
 def orainceput(l):
     return l[1]
 f=open("spectacole.txt")
 l=[]
 crt=1
 for linie in f:
     aux=linie.split("-")
     l.append((crt,aux[0],aux[1]))
     crt+=1
 
 f.close()
 l.sort(key=orainceput)
 sali=queue.PriorityQueue()
 sali.put((l[0][2],list((l[0],))))
 for k in range(1,len(l)):
     min_timp_final=sali.get()
     if l[k][1]>=min_timp_final[0]:
         min_timp_final[1].append(l[k])
         sali.put((l[k][2],min_timp_final[1]))
     else:
         sali.put(min_timp_final)
         sali.put((l[k][2],list((l[k],))))
 g=open("programare.txt",'w')
 g.write("Numar minim de sali:"+str(sali.qsize())+"\n")
 scrt=1
 while not sali.empty():
     sala=sali.get()
     g.write("\nSala"+str(scrt)+":\n")
     for l in sala[1]:
         g.write("\t"+l[1]+"-"+l[2]+"Spectacol"+str(l[0])+"\n")
     scrt+=1
 f.close()
