import random
print("Угадай число от 1 до 100")
attempts=0
ishut=random.randint(1, 100)
try:
    iskomoe=int(input("Введите число: "))
except:
    print("Произошла ошибка, повторите попытку")
else:
    while True:
        attempts+=1
        if iskomoe<ishut:
            print("Больше")
        elif iskomoe>ishut:
            print("меньше")
        else:
            print(f"Ты угадал искомое число за {attempts} поыток. Искомое число было {ishut}")
            break
        iskomoe=int(input('Повтори попытку: '))