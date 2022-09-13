import random
import time
from datetime import datetime
import sys
'''주어진 수만큼의 난수를 만드는 함수'''
def random_number(a):
    if a=='exit':
        sys.exit()

    b=int(a)
    number = set()
    while True:
        if len(number) == b:
            break
        else:
            r_n = random.randint(0,9)
            number.add(r_n)

    return number
'''유저가 입력한 수와 난수를 비교해서 볼과 스트라이크를 판별하는 함수'''
def number_check(a,b):
        strike=0
        for i in range(len(a)):
            if a[i] == b[i]:
                strike = strike+1
        g= len([val for val in a if val in b])
        ball = g - strike

        return ball, strike
'''전체적인 코드의 작동을 하는 함수'''
def main():
    start_time = time.time()
    k=0
    f=[]
    random_number_list=list(random_number((input('몇자릿수의 게임을 하실지 입력해주세요:'))))
    user_number=input('공백으로 구분해서 숫자를 입력해주세요:')
    if user_number=='exit':
        sys.exit()
    user_number_list=list(map(int,user_number.split()))
    '''난수 확인용 출력(과제 제출시 삭제예정)'''
    print(f'유저가 입력한 숫자:{user_number_list}')
    print(f'컴퓨터가 생성한 난수:{random_number_list}')
    while user_number_list != random_number_list:
        k=k+1
        f = (number_check(user_number_list,random_number_list))
        print(f'{f[0]}볼, {f[1]}스트라이크 입니다')
        user_number = input('다시 숫자를 입력해주세요:')
        if user_number == 'exit':
            sys.exit()
        user_number_list=list(map(int,user_number.split()))
    if user_number_list == random_number_list:
        k = k + 1
        end_time = time.time()
        print('정답입니다!')
        print(f'숫자를 입력한 횟수:{k}')
        print(f"사용자가 게임을 시작해서 정답을 맞추기까지 소요된 시간 : {end_time - start_time:.0f}초")
        print(f'{datetime.now()}')


