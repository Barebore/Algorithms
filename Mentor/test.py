class Gtlt:
    def __gt__(self, other):
        return True

    def __lt__(self, other):
        return False


class Triangle(Gtlt):
    pass
    
class Square(Gtlt):
    pass

class Other(Triangle, Square):
    pass

a = Triangle()
b = Square()


c = Other()

print(int.__super__.__name__)
print(c.mro)

if a>b:
    print("a is bigger")