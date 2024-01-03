#2
#m=int(input("m="))
#a=[]
#for i in range(m):
#    a.append(int(input("el=")))
#n=int(input("n="))
#b=[]
#for i in range(n):
#    b.append(int(input("el2=")))

#a.sort(reverse=True)
#b.sort(reverse=True)
#s=0
#i=0
#while a[i]>0:
#    s=s+a[i]*b[i]
#    i+=1
#for k in range(-1,-i,-1):
#    s+=a[k]*b[k]
#print(s)

#4

def afis(n):
    global t
    for i in range(1,n+1):
        ok = 1
        if x[i] > t:
            ok=0
        if ok == 1:
            print(x[i],end=" ")
    print('\n')

def back(i,s):
    for j in range(1,s+1):
        x[i]=j
        if x[i]==s:
            afis(i)
        else:
            back(i+1,s-x[i])

n=5
t=3
nr=0
x = [0 for i in range(100)]
print(back(1,n))


