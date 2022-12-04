class HandlerGET:
    def __call__(self, get_dict):
        pass

@HandlerGET
def contact(request):
    return "Сергей Балакирев"