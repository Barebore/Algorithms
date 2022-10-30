class AppStore:
    app_lst = []
    def add_application(self, app):
        self.app_lst.append(app)
    
    def remove_application(self,app):
        del self.app_lst[self.app_lst.index(app)]

    def block_application(self,app):
        self.app_lst[self.app_lst.index(app)].blocked = True

    def total_apps(self):
        return len(self.app_lst)

class Application:

    def __init__(self,name, blocked = False):
        self.name = name
        self.blocked = False


store = AppStore()
app_youtube = Application("Youtube")
assert app_youtube.blocked == False, "начальное значение blocked должно быть равно False"
store.add_application(app_youtube)
store.block_application(app_youtube)
assert app_youtube.name == "Youtube" and app_youtube.blocked == True, "неверные значения локальных атрибутов объекта класса Application"
app_stepik = Application("Stepik")
store.add_application(app_stepik)
assert store.total_apps() == 2, "неверное число приложений в магазине"
store.remove_application(app_youtube)
assert store.total_apps() == 1, "неверное число приложений в магазине, некорректно работает метод remove_application"