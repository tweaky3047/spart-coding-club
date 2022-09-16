a=int(input())
k=1
while True:
    a = a-k
    if a<=0:
        a=a+k
        break
    k=k+1

b=a
if k%2==0:

    print(str(1+(a-1))+'/'+str(k+1-a))
else:
    b = a - 1
    print(str(k+1-a) + '/' + str(1+(a-1)))

