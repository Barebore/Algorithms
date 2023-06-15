class Ellipse:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        if x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

    def __bool__(self):
        try:
            return self.x1 != 0 and self.y1 != 0 and self.x2 != 0 and self.y2 != 0
        except:
            pass
        return False
    
    def get_coords(self):
        if self.__bool__():
            return (self.x1, self.y1, self.x2, self.y2)
        else:
            raise AttributeError('нет координат для извлечения')
        
lst_geom = []
lst_geom.append(Ellipse())
lst_geom.append(Ellipse())
lst_geom.append(Ellipse(1,2,3,4))
lst_geom.append(Ellipse(1,2,3,4))

for i in lst_geom:
    print(i.get_coords())