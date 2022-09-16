a=int(input())
s=[0, 1]
k=0
for i in range(2,a+1):
    k=s[i-1]+s[i-2]
    s.append(k)

print(s[a])