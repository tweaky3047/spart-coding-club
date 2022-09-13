N=int(input())
k=0
for i in range(N+1):

    if 1 <= i <10:
        k=k+1
    elif 10 <= i <100:
        k = k + 1
    elif 100 <= i <1000:
        a=i//100
        b=(i//10)%10
        c=(i%100)%10
        if int(a-b) == int(b-c):
            k=k+1
        else:
            continue
    else:
        continue

print(k)