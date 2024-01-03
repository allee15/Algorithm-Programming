#2
#n=int(input("n="))
#ls=[]
#li=[]
#for i in range(n):
#    s=input("bat=")
#    t=[int(x) for x in s.split()]
#    t.append(i+1)
#    tt=tuple(t)
#    ls.append(tt)
#ls.sort(key=lambda t:(t[0]))
#print(ls)
#ultim=ls[0]
#for i in range(1,n):
#    if ls[i][0]>ultim[0] and ls[i][0]+ls[i][1]>ultim[0]+ultim[1] and ls[i][0]>ultim[0]+ultim[1]:
#        ultim=ls[i]
#    else:
#        print(ls[i],sep=" ")


#4

#def comb(k):
#    global fete,baieti,ok
#    if k==s+1:
#        if fete==baieti:
#            print(*x[1:k],sep=", ")
#            ok=1
#    else:
#        for i in range(x[k-1], n + 1):
#            x[k]=i
#            if i<=nrf:
#                fete+=1
#            else:
#                baieti+=1
#            if x[k] not in x[:k] and fete<=s//2 and baieti<= s//2:
#                comb(k+1)
#            if i<=nrf:
#                fete-=1
#            else:
#                baieti-=1
#            

           
#nrf=int(input("nrf="))
#nrb=int(input("nrb="))
#s=int(input("s="))
#n=nrf+nrb
#fete=0
#baieti=0
#x=[0 for i in range(s+1)]
#comb(1)
#if ok==0:
#    print("imposibil")

#3

n=int(input("n="))
s=input("s=")
l=[x for x in s.split()]
l.sort()
ultim=l[0]
print(l,ultim)
for x in l:
    if chr(ord(x[0])+1)==chr(ord(ultim[len(ultim)-1])):
        ultim=x
    else:
        print(x,sep=" ")
