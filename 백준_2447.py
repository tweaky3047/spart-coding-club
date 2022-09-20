import math
a = int(input())
b = int(math.log(a,3))
k =''
print(b)
k=['']*a

def star():
    k = [''] * 3
    for q in range(3):
        for i in range(3):
            if i==1 and q==1:
                k[i]=(k[i]+' ')
            else:
                k[q] = k[q]+'*'
    print(k)
    return k

def stars(j,l):
    t=['']*(3**l)
    for q in range(3):

        for i in range(3):

            if i==1 and q==1:
                for i in range(3):
                    t[i+q*3]=t[i+q*3]+' '*3*(l-1)
            else:
                for i in range(3):
                    t[i+q*3] = t[i+q*3] + j[i]


    return t

o=stars(star(),2)

for i in range(2,b+1):
    o=stars(o,i)

for i in o:
    print(i)


