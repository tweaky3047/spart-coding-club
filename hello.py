a=int(input())
k=0
A=a
while True:
    if A<10:
        k = k + 1
        g='0'+str(A)
        b = str(g)[0]
        c = str(g)[1]
        d = int(b) + int(c)
        if d>=10:
            e = int(str(g)[1] + str(d)[1])
        else:
            e = int(str(g)[1] + str(d)[0])

    else:
        k = k + 1
        b=str(A)[0]
        c=str(A)[1]
        d=int(b)+int(c)
        if d >= 10:
            e = int(str(A)[1] + str(d)[1])
        else:
            e = int(str(A)[1] + str(d)[0])

    if a==e:
        print(k)
        break
    else:
        A = e



