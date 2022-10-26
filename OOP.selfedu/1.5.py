import random

class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a,b)
        self.ep = (c,d)
        
class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a,b)
        self.ep = (c,d)
        
class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a,b)
        self.ep = (c,d)
        

class_lst = [Line, Rect, Ellipse]
rr = random.randint
elements = [class_lst[rr(0,2)](rr(0,10), rr(0,10), rr(0,10), rr(0,10)) for _ in range(217)]
#print(elements)

for i in elements:
    if isinstance(i,Line):
        #print(i)
        #print(i.sp, i.ep)
        i.sp = 0
        i.ep = 0
      #  print(i.sp, i.ep)