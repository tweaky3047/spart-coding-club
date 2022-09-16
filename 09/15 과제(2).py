for i in range(5):
    b=input()
    if b=='exit':
        break
    a='a'
    try:
        a=int(b)
    except ValueError:
        print(f'입력한 문자는 {b}입니다')
        continue
    a=a*2
    print(a)