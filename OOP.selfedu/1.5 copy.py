# здесь объявите класс TriangleChecker
class TriangleChecker:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        a = self.a
        b = self.b
        c = self.c
        if type(a) not in (float,int) or type(b) not in (float,int) or type(c) not in (float,int) or a <= 0 or b<= 0 or c<=0:
            return 1
        if not((a + b > c) and (b + c > a) and (a + c > b)):
            return 2
        return 3
            
    
a, b, c = ([5],5,5) # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран

tr = TriangleChecker(a,b,c)
print(tr.is_triangle())