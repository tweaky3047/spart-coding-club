common=[]
common_=[]
for i in range(1,10001):
    common.append(i)
for i in common:
    if 1 <= i < 10:
        common_.append(i + i)
    elif 10 <= i < 100:
        common_.append(i + (i // 10) + (i % 10))
    elif 100 <= i < 1000:
        common_.append(i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]))
    elif 1000 <= i < 10000:
        common_.append(i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3]))

a=list(set(common)-set(common_))
list.sort(a)
for i in a:
    print(i)

