class SmartPhone:
    def __init__(self, model):
       self.model = model
       self.apps = []

    def add_app(self, app):
        for i in self.apps:
            if app.name == i.name:
                return
        self.apps.append(app)

    def remove_app(self, app):
        del self.apps[self.apps.index(app)]

class AppVK:
    def __init__(self, name = 'Вконтакте'):
        self.name = name

class AppYouTube:
    def __init__(self, memory_max,name = 'Youtube'):
        self.name = name
        self.memory_max = memory_max

class AppPhone:
    def __init__(self, phone_list, name = 'Phone'):
        self.name = name
        self.phone_list = phone_list
    
sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)