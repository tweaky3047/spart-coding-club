import math
a=int(input())
b=int(input())
t=[]
f=[x for x in range(a,b+1)]
n = b
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
    while i * j <= n:
        array[i * j] = False
        j += 1


for i in range(2, n + 1):
    if array[i]:
       t.append(i)


f_sub_t = [val for val in f if val in t]
if len(f_sub_t)==0:
    print(-1)
else:
    print(sum(f_sub_t))
    print(f_sub_t[0])
