import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
a = int(input())

count = [0]*10001
for i in range(a):
    count[int(sys.stdin.readline())] += 1

for i in range(10001):
    for t in range(count[i]):
        print(i)






