class Calc():
    def set_number(self):
        try:
            self.a,self.b=map(int,input().split())
        except ValueError:
            print('숫자만 입력 가능합니다')
    def plus(self):
        try:
            k = self.a + self.b
            return k
        except:

            return '숫자만 입력 가능합니다'
    def minus(self):
        try:
            k = self.a - self.b
            return k
        except:
            return '숫자만 입력 가능합니다'
    def multiple(self):
        try:
            k = self.a * self.b
            return k
        except:
            return '숫자만 입력 가능합니다'
    def divide(self):
        try:
            k = self.a / self.b
            return k
        except ZeroDivisionError:
            return '0으로 나눌 수 없습니다'
        except:
            return '숫자만 입력 가능합니다'


calc = Calc()
calc.set_number()
print(calc.plus()) # 더한 값
print(calc.minus()) # 뺀 값
print(calc.multiple()) # 곱한 값
print(calc.divide()) # 나눈 값

