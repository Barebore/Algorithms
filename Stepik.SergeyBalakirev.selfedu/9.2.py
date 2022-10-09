def get_list():
    for x in [1,2,3,4]:
        yield x

a = get_list()
for x in a:
    print(x)
