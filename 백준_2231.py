a = int(input())

for i in range(1,a+1):
    if i<=9:
        if a==i+i:
            print(i)
            break
    elif 10 <= i <100:
        h = str(i)
        if a==(i + int(h[0]) + int(h[1]) ):
            print(i)
            break
    elif  100 <= i < 1000:
        h = str(i)
        if a == (i + int(h[0]) + int(h[1]) + int(h[2]) ):
            print(i)
            break
    elif  1000 <= i < 10000:
        h = str(i)
        if a == (i + int(h[0]) + int(h[1]) + int(h[2]) + int(h[3])):
            print(i)
            break
    elif  10000 <= i < 100000:
        h=str(i)
        if a == (i + int(h[0]) + int(h[1]) + int(h[2])+int(h[3])+int(h[4])):
            print(i)
            break
    elif 100000 <= i < 1000000:
        h = str(i)
        if a == (i + int(h[0]) + int(h[1]) + int(h[2])+int(h[3])+int(h[4])+int(h[5])):
            print(i)
            break
else:
    print(0)


