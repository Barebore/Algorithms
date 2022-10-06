def func_show(func):
    def textfunc(*args,**kwargs):
        print('Площадь прямоугольника:', )
        result = 'Площадь прямоугльника:' + str(func(*args,**kwargs))
        return result
    
    return textfunc

@func_show
def get_sq(width, height):
        return  width*height

width = 8
height = 11
f = get_sq(width, height)






