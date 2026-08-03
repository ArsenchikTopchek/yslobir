import random
def check_dice(number):
    if number == 1 or number == 2:
        return 'Неудачный бросок'
    elif 3 <= number <= 5:
        return 'Обычный бросок'
    elif number == 6:
        return 'Отличный бросок'
dice = random.randint(1, 6)
print('На кубике выпало: dice')
print(check_dice(dice))