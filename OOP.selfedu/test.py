a = [1, "abc", -5, 7.68, True]

b = [value for value in a if (isinstance(value, int) or isinstance(value, float)) and not isinstance(value, bool)]
print(b)