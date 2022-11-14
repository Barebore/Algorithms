class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, *args, **kwargs):
        for i in args:
            if i.rsplit('.')[-1] in self.extensions:
                return True
            return False

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)
        
        


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg",
             "eq_1.png", "eq_2.png", "my.html", "data.shtml"]

fs = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]
acceptor = ImageFileAcceptor(("jpg", "png"))
res = filter(acceptor, fs)
assert set(res) == set(["boat.jpg", "web.png", "ava.8.jpg", "eq_1.png", "eq_2.png"]), "с помощью объекта класса ImageFileAcceptor был сформирован неверный список файлов"
acceptor = ImageFileAcceptor(("jpeg", "html"))
res = filter(acceptor, fs)
print(acceptor.extensions)
print(set(res))
# assert set(res) == set(["forest.jpeg", "my.html"]), "с помощью объекта класса ImageFileAcceptor был сформирован неверный список файлов"