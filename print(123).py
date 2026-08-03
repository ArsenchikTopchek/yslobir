import random
def check_number(number):
    if number == 0:
        return 'Ноль'
    elif number > 0:
        if number % 2 == 0:
            return 'Положительное четное'
        else:
            return 'Положительное нечетное'
    else:
        return 'Отрицательное'
number = random.randint(-10, 10)

print('Выпало число: number')
print(check_number(number))