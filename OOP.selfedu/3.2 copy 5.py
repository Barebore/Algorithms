class HandlerGET:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, *args, **kwargs):
        return self.get(self.__fn, *args, **kwargs)

    def get(self, func, request, *args, **kwargs):
        if request['method']:
            return f'{request["method"]}: {func(*args, **kwargs)}'

@HandlerGET
def contact(request):
    return "Сергей Балакирев"

res = contact({"method": "GET", "url": "contact.html"})
print(res)