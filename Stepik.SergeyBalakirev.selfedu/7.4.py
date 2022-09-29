def check_password(str, chars =  "$%!?@#"):
    flag = 0
    if len(str) >= 8:        
        for char in chars:
            if char in str:
                flag = 1
        if flag:
            return bool(flag)
        else:
            return bool(flag)
    else:
        return bool(flag)
        
print(check_password('1234567ghjghj'))