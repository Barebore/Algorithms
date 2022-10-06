# put your python code here
def make_dict(func):
    def wrapper(*args, **kwargs):
        s1, s2 = func(*args, **kwargs)
        d = dict(s1,s2)
        result = d
        return result
    
    return wrapper

@make_dict
def split_two_str(s1,s2):
    s1 = s1.split()
    s2 = s2.split()
    return s1, s2
    
s1 = input()
s2 = input()    
d = split_two_str(s1,s2)
print(*sorted(d.items()))

