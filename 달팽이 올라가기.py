a, b, c = map(int, input().split())
s=0
k=0
s = c%(a-b)
k = c//(a-b)
if s>a:
    print(k+1)
if k>0:
    print(s)
else:
    print(s-1)
ss