def is_pangram(s):
    from string import ascii_lowercase as lst
    for char in lst:
        if char not in s.replace(' ', '').replace('.', '').replace(',', '').lower():
            return False
    return Trueå