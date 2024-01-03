#1
#n=int(input("n="))
#linie=input("linie=")
#nr=0
#l=[int(x) for x in linie.split()]
#l.sort(reverse=False)
#for i in range(1,n):
#    l[i]+=l[i-1]
#nr=sum(l[:n])
#print(nr,"//",n)

#2
n=int(input("n="))
ls=[]
s=[int(x) for x in input("inceput=").split()]
f=[int(x) for x in input("final=").split()]
for i in range(n):
    t=(s[i],f[i])
    ls.append(t)
ls.sort(key= lambda t:(t[1]))

ultim=ls[0][0]
nr=1
lp=[]
while ls!=[]:
    lp.append(ls[0])
    for k in range(1,n):
        if ls[k][0]>ultim:
            lp.append(ls[k])
            ultim=ls[k][0]
            ls.pop(k)
    print(nr)
    print(lp)
    nr+=1
    lp=[]




