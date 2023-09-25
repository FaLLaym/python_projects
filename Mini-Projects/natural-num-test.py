number = int(input("Введите натуральное число: \n"))

def checkNum(num : int) -> set|bool:
    dividers = set()
    try:
        for x in range(1, int(num**.5)+1):
            if num % x:
                dividers |= {x, num//x}
        return dividers
    except:
        return 0

print(checkNum(number))