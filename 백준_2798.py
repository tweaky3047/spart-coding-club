a,b=map(int,input().split())
c=[x for x in map(int,input().split())]

e=[]
for i in c:
    d=c[:]
    d.remove(i)

    for j in d:
        d.remove(j)

        for k in d:
            g=[i,j,k]
            e.append(g)
j=[]

for i in e:
    if sum(i) <= b:
        j.append(sum(i))
print(max(j))