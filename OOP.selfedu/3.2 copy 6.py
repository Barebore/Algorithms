class HandlerGET:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, *args, **kwargs):
        return self.get(self.__fn, *args, **kwargs)

    def get(self, func, request, *args, **kwargs):
        pass

    def post(self, func, request, *args, **kwargs):
        pass

@HandlerGET(methods=('GET', 'POST'))
def contact(request):
    return "главная страница сайта"


res = contact({"method": "POST", "url": "contact.html"})
