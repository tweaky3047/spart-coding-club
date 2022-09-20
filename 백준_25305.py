a,b=map(int,input().split())
c=[x for x in map(int,input().split())]
c.sort()
c.reverse()

print(c[b-1])