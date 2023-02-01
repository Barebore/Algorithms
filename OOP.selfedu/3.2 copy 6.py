class HandlerGET:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, *args, **kwargs):
        return self.get(self.__fn, *args, **kwargs)

    def get(self, func, request, *args, **kwargs):
        if request == {}:
            return 'GET: ' + func(request)
        if request:
            #print(request)
            if request is None or request['method']=='GET':
                return f'{request["method"]}: {func(request)}'
            return None
        return None

@HandlerGET
def index(request):
    return "главная страница сайта"
res = index({"method": "GET"})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
res = index({"method": "POST"})
#print(res)
assert res is None, "декорированная функция вернула неверные данные"
res = index({"method": "POST2"})
assert res is None, "декорированная функция вернула неверные данные"
res = index({})
print(res)
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"