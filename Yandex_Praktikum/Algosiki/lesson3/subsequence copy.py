a = input()
b = input()
start = 0
def verify(a,b):
    start = 0
    for word in a:
        if word in b:
            start = b.index(word)
            b = b[start:]
        else:
            return False
    return True

print(verify(a,b))

