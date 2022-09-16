
d=int(input())
for i in range(d):
    a, b, c = map(int, input().split())
    k=c//a
    n=c%a
    if k>0:
        if n>10:
            print(str(k)+str(n))
        else:
            print(str(k) +'0'+ str(n))
    else:
        if n>10:
            print('1'+str(n))
        else:
            print('1'+'0'+ str(n))