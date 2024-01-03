#PERMUTARI#
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


#COMBINARI#
def comb(k):
    if k==m:
        print(*x)
    else:
        if k==0:
            start=1
        else:
            start=x[k-1]+1
        for i in range(start, n + 1):
            x[k] = i
            comb(k + 1)

n=5
m=3
x=[0 for i in range(m)]
print("COMBINARILE SUNT: \n")
comb(0)

#ARANJAMENTE#
def aranj(k):
    if k==m:
        print(*x)
    else:
        for i in range(1,n+1):
            x[k]=i

            if x[k] not in x[:k]:
                aranj(k+1)

n=4
m=3
x=[0 for i in range(m)]
print("ARANJAMENTELE SUNT: \n")
aranj(0)

#SUBMULTIMI#
def subm(k):
    if k==n:
        print([a[i] for i in range(n) if x[i]==1])
    else:
        for i in range(0,2):
            x[k]=i
            subm(k+1)

a=[3,1,7,9]
n=len(a)
x=[0 for i in range(n)]
print("SUBMULTIMILE SUNT: \n")
subm(0)

#PARTITII#
def part(k):
    if sum(x[:k]) == n:
        print(*x[:k])
    else:
        if k==0:
            start=1
        else:
            start=x[k-1]
        for i in range(start,n+1):
            x[k]=i
            if sum(x[:k+1])<=n:
                part(k+1)

n=4
x=[0 for i in range(n)]
print("PARTITIILE SUNT: \n")
part(0)


#TOATE PARTITIILE#

def afis(n):
    for i in range(1,n+1):
        print(x[i])
    print('\n')

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
x = [0 for i in range(100)]
print("PARTITIILE COMPLETE SUNT: \n")
print(back(1,n))

#PRODUS CARTEZIAN#
def cartesianProduct(set_a, set_b):
    result =[]
    for i in range(0, len(set_a)):
        for j in range(0, len(set_b)):
 
            if type(set_a[i]) != list:        
                set_a[i] = [set_a[i]]
                 

            temp = [num for num in set_a[i]]
             

            temp.append(set_b[j])            
            result.append(temp) 
             
    return result
 

def Cartesian(list_a, n):

    temp = list_a[0]
     
    for i in range(1, n):
        temp = cartesianProduct(temp, list_a[i])
         
    print(temp)
 

list_a = [[1, 2],         
          ['A'],        
          ['x', 'y', 'z']]  

n = len(list_a)

Cartesian(list_a, n)
