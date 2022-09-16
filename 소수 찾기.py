import math
a=int(input())
f=0
k=0
b=list(map(int,input().split()))

def is_prime_num(n):
    if n==1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False


    return True
for i in b:
    if is_prime_num(i):
        k=k+1

print(k)