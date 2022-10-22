def get_list_dig(lst):
    return list(filter(lambda x: type(x) in (int,float), lst))

ad = [1,2,3,'d']

print(get_list_dig(ad))

