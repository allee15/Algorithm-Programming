#def aparitii(*numere):
#    dict={}
#    c=-1
#    l=[]
#    for element in numere:
#        while c<10:
#            c+=1
#            f=0
#            for i in element:
#                if i==c:
#                    f+=1
#            if f>0:
#                t=[c,f]
#                tt=tuple(t)
#                l.append(tt)
#        dict[element]=l
#    return dict

#print(aparitii(1011,234,8158558))

#m=[[1,2,3],[4,5,6],[7,8,9]]

#numere=[m[i][j]**2 for i in len(m) for j in len(m) if i==j]
#print(numere)

n=int(input("n="))
t=int(input("t="))
l=[]
for i in range(n):
    s=input("el=")
    t=[float(f) for f in s.split()]
    tt=tuple(t)
    l.append(tt)
l.sort(key=lambda t:(t[0]))
sol=[]

sol.append(l[0][0])
s=l[0][0]*l[0][1]
cant=l[0][0]
for i in range(1,n):
    if s/cant==t:
        print(format(sol,"3f"))
        i=n
        else:
            s+=l[i][0]*l[i][1]
            cant+=l[i][0]
            x=l[i][0]
            if s/cant>t:
                while s/cant>t:
                    s-=1
                    cant-=1
                    x-=1
            sol.append(x)


