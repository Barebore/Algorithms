class FileAcceptor:
    def __init__(self, *args):
        self.extensions = list(args)

    def __add__(self, other):
        result = self.extensions + other.extensions
        return FileAcceptor(*result)
    
    def __call__(self, value):
        return value.split(".")[-1] in self.extensions
    

acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")

# print(acceptor1.extensions)
# print(acceptor2.extensions)
# print(acceptor12.extensions)

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))

# filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]