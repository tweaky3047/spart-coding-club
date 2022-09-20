import sys
import math
a = int(sys.stdin.readline())
b=[]
e={}
for i in range(a):
    b.append(int(sys.stdin.readline()))
b.sort()
for i in b:
    if i not in e:
        e[i]=1
    else:
        e[i]+=1
max(e,key=e.get)
t=[k for k,v in e.items() if max(e.values()) == v]
t.sort()
avg = round(sum(b)/a)
middle = b[(a//2)]
range = max(b)-min(b)
print(avg)
print(middle)
if len(t)==1:
    print(t[0])
else:
    print(t[1])
print(range)