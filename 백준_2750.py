import sys
sys.setrecursionlimit(10**6)
a=int(sys.stdin.readline())
b=[]
for i in range(a):
    b.append(int(sys.stdin.readline()))
b.sort()

for i in b:
    print(i)