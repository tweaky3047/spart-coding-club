class Area():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def square(self):
        return self.a*self.b
    def triangle(self):
        return self.a*self.b/2
    def circle(self):
        return (self.a/2)*3.14




area = Area(10, 20)
print(area.square()) # 사각형의 넓이
print(area.triangle()) # 삼각형의 넓이
print(area.circle()) # 원의 넓이