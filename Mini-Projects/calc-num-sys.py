import string

number = int(input("Введите число в десятичной системе счисления: \n"))
num_sys = int(input("Введите систему счисления:\n"))

def transformator(num : int, base : int, upper=False) -> str|bool:
    digits = '0123456789' + ''.join(string.ascii_lowercase)
    if base > len(digits):
        return 0
    rs = ''
    while num:
        rs += digits[num%base]
        num //= base
    return rs.upper() if upper else rs

print(transformator(number, num_sys))