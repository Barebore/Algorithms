a = input()
b = input()
start = 0
def verify(a, b):
    start = 0
    for word in a:
        try:
            start = b.index(word, start) + 1
        except ValueError:
            return False
    return True

print(verify(a,b))

