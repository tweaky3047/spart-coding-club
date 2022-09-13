def bee_house(r):
    if r == 1:
        return print(1)
    a = 1
    i = 1
    k=6
    while True:
        a = a + k
        i = i + 1
        k= k+6
        if r <= a:
            print(i)
            break





b = int(input())
bee_house(b)


