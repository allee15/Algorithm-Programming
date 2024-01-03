#1 Se dă o sumă S şi n tipuri de monede având valorile v1, v2, ..., vnlei
#(un număr nelimitat de valori de fiecare tip). 
#Se cer toate modalităţile de plată a 
#sumei S utilizând aceste monede.Exemplu: Pentru S=20 şi n=3 tipuri de monede, 
#cu valorile v1=1,v2=5, v3=10 putem avea următoarele modalităţi de plată (pentru fie
#care monedă de la 1 la n se afişează numărul de monezi de acest tip care se plătesc):

#def back(k,suma):
#    if k==n:
#        if suma==s:
#            print(*x)
#    else:
#        for i in range(mini+1):
#            x[k]=i
#            suma+=x[k]*v[k]
#            back(k+1,suma)
#            suma-=x[k]*v[k]
#            x[k]=0

#n=3
#v=[1,5,10]
#s=20
#x=[0 for i in range(n)]
#mini=s//min(v)
#back(0,0)

#2 Se dau n mulțimi (elementele fiecărei mulțimi se dau pe o linie, separate prin spațiu). 
#Să se afișeze elementele produsului cartezian al celor n mulțimi

#def cartesianProduct(set_a, set_b):
#    result =[]
#    for i in range(0, len(set_a)):
#        for j in range(0, len(set_b)):
 
#            if type(set_a[i]) != list:        
#                set_a[i] = [set_a[i]]
                 

#            temp = [num for num in set_a[i]]
             

#            temp.append(set_b[j])            
#            result.append(temp) 
             
#    return result
 

#def Cartesian(list_a, n):

#    temp = list_a[0]
     
#    for i in range(1, n):
#        temp = cartesianProduct(temp, list_a[i])
         
#    print(temp)
 

#list_a = [[1,4],         
#          [2,6],        
#          [10,11,12]]  

#n = len(list_a)

#Cartesian(list_a, n)

#3 Pentru elaborarea unui test de aptitudini avem un set de n întrebări, fiecare fiind cotată cu un număr de puncte dat. 
#Să se elaboreze toate chestionarele având a întrebări distincte,
# fiecare chestionar totalizând p puncte. Întrebările sunt date prin număr şi punctaj. 
#Nu se ţine cont de ordinea întrebărilor în chestionar 
#(de exemplu chestionarul cu întrebările 1 şi 2 este acelaşi cu chestionarul cu întrebările 2 şi 1)

def back(k):
    if k == a:
        sum = 0
        for i in x[:a]:
            sum+= pct[i-1]
        if sum == p:
            print(*x[:a])
    for i in range(1,n+1):
        if i not in x:
            if i > x[k-1]:
                x[k] = i
                back(k+1)
                x[k] = 0
n = 6
a = 3
p = 10
x = [0 for x in range(n)]
pct = [1,4,2,3,5,4]
back(0)

#4 Să se descompună un număr natural n în toate modurile posibile distincte ca 
#sumă de numere prime  (de  exemplu,  pentru  n  =  10  descompunerile  sunt  
#2+2+2+2+2,  2+2+3+3,  2+3+5,  5+5, 3+7).

#def primenumber(p):
#    ok=0
#    for i in range(2,p):
#        if p%i==0:
#            ok+=1
#    if ok==0:
#        return 1
#    else:
#        return 0

#def part(k):
#    if sum(x[:k]) == n:
#        print(*x[:k],sep="+ ")
#    else:
#        if k==0:
#            start=1
#        else:
#            start=x[k-1]
#        for i in range(start,n+1):
#            if primenumber(i)==1 and i>=x[k-1] and sum(x[:k])+i<=n:
#                x[k]=i
#                part(k+1)
#                x[k]=0
            

#n=10
#x=[0 for i in range(n)]
#part(0)
