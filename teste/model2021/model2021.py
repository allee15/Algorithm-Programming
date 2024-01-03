#1
#a

#def divizori(*n):
#    dict={}
#    for i in n:
#        l=[]
#        s=i
#        for j in range(2,i):
#            if s%j==0:
#                while s%j==0:
#                    s=s//j
#                l.append(j)
#        dict[i]=l
#    return dict

#print(divizori(50,21))

#b

#liste_10=[x for x in ("abcdefghij")]
#print(liste_10)

#2

#n=int(input("n="))
#nr=0
#ls=[]
#s=[int(x) for x in input("inceput=").split()]
#f=[int(x) for x in input("final=").split()]
#for i in range(n):
#    t=(s[i],f[i])
#    ls.append(t)
#ls.sort(key= lambda t:(t[1]))
#print(ls)
#ultim=ls[0][0]
#for k in range(1,n):
#    if ls[k][0]>ultim:
#        nr+=1
#        ultim=ls[k][0]
#print(nr)

#3
def perm(k):
    if k==n: 
        print(*x)
    else:
        for i in range(1,n+1):
            x[k]=i
            if x[k] not in x[:k]:
                perm(k+1)
           
n=4
x=[0 for i in range(n)]
print("PERMUTARILE SUNT: \n")
perm(0)

        


