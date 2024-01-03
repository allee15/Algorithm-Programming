proiecte.sort(key=sortare, reverse=True)
 print(proiecte)
 p = []
 profit = 0
 zi_max = max(m[1] for m in proiecte)
 planificare = {z: None for z in range(1, zi_max + 1)}
 for proiect in proiecte:
     for z in range(proiect[1], 0, -1):
         if planificare[z] is None:
             planificare[z] = proiect
             profit += proiect[2]
             break

 g = open("proiecte.out")
 for z in planificare:
     if planificare[z]!=None:
         g.write("Ziua" + str(z) + ":" + planificare[z][0] + " " + str(planificare[z][2]) + "\n")
 g.write("\nProfit maxim:" + str(profit))
 g.close()
