n=int(input("nr coloane: "))
m=int(input("nr linii: "))
mat = [[int(x) for x in input("linia: ").split()]for i in range(m)]
sol=mat


start_i=3
start_j=1

v_poz=[]


i=1
for linie in sol[i:]:
    for j in range(len(linie)):
        if j != 0 and j != n-1:
            sol[i][j]=mat[i][j]+min(sol[i-1][j-1],sol[i-1][j],sol[i-1][j+1])
        elif j==0:
            sol[i][j]=mat[i][j]+min(sol[i-1][j],sol[i-1][j+1])
        elif j==n-1:
            sol[i][j]=mat[i][j]+min(sol[i-1][j],sol[i-1][j-1])
    if i < m-1:
        i += 1

i=0
for linie in sol[i:m-1]:
    minim = min(linie)
    for j in range(len(linie)):
        if sol[i][j]==minim:
            v_poz.append([i,j])
    if i < m-2:
        i += 1
        
print(sol)
v_poz.append([start_i,start_j])
for x in reversed(v_poz):
    print(*x)
    
minim = min(mat[m-1])
c=0
for x in mat[m-1]:
    if x == minim:
        c+=1

if c > 1:
    print("traseul nu e unic")
