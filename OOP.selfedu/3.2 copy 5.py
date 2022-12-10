class HandlerGET:
    def __init__(self, func) -> None:
        self.__func = func
    def __call__(self, get_dict):
        pass

@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({'method': 'GET', 'url': 'contact.html'})