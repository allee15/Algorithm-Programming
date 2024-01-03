#1 a
#def divizori(n):
#    d=2
#    dict={}
#    while n>1:
#        x=0
#        while n%d==0:
#            n=n//d
#            x+=1
#        if x>0:
#            dict[d]=x
#        d+=1
#    return dict

#b

#def ceva(dict):
#    x=1
#    for i in dict:
#        s=dict[i]
#        while s>0:
#            x=x*i
#            s-=1
#    return x

#c
#def altceva(a,b):
#    dict1=divizori(a)
#    dict2=divizori(b)
#    dict3={}
#    for i in dict1.keys():
#        if i in dict2.keys():
#            dict3[i]=min(dict1[i],dict2[i])
#    x=ceva(dict3)
#    return x

#a=int(input("a="))
#b=int(input("b="))
#print(altceva(a,b))

#2
#n=int(input("n="))
#ls=[]
#with open("spectacole.in","r") as fin:
#    s=fin.readline()
#    while s:
#        t=[int(x) for x in s.split()]
#        tt=tuple(t)
#        ls.append(tt)
#        s=fin.readline()
#nr=1
#ls.sort(key=lambda t:(t[1]))
#ultim=ls[0][0]
#l=[]
#l.append(ls[0])
#for k in range(1,n):
#    if ls[k][0]>=ultim:
#        nr+=1
#        ultim=ls[k][1]
#        l.append(ls[k])
#print(l)
#print(nr)

#4
def perm(k,m):
    if k==n:
        if sum(x)>=r and x<=m and max(x)<=max(m):
            print(*x)
    else:
        for i in range(1,sum(m)+1):
            x[k]=i
            perm(k+1,m)
           
n=int(input("n="))
m=[]
r=int(input("r="))
for i in range(n):
    f=input("el=")
    m.append(int(f))
x=[0 for i in range(n)]
print("PERMUTARILE SUNT: \n")
perm(0,m)



        
            

