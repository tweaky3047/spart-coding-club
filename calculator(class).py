class Calc():
    def set_number(self):
        self.a,self.b=map(int,input().split())
    def plus(self):
        return self.a + self.b
    def minus(self):
        return self.a - self.b
    def multiple(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b

calc = Calc()
calc.set_number()
print(calc.plus()) # 더한 값
print(calc.minus()) # 뺀 값
print(calc.multiple()) # 곱한 값
print(calc.divide()) # 나눈 값