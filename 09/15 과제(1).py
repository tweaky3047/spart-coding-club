a=int(input())
def get_grade(a):
    if a >= 91:
        print('A')
    elif 90>=a>=81:
        print('B')
    elif 80 >= a >= 71:
        print('c')
    else:
        print('F')
get_grade(a)