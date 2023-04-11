input_str = input()
input_str = input_str.replace(' ','')
input_str = ''.join(e for e in input_str if e.isalnum())
input_str = input_str.lower()
l = len(input_str)
half_str1 = input_str[: l // 2]
half_str2 = input_str[:l//2 if l % 2 == 1 else l//2-1:-1]
print(half_str1, half_str2)
print(half_str1 == half_str2)
