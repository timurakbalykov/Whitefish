import random       # Для генерации случайного числа

lowDigit = 10       # Нижняя граница случайного числа
hightDigit = 50     # Верхняя граница случайного числа
digit = 0           # Загаданное число

countInput = 0      # Количество попыток угадать
win = False         # Угадал текущее число?
playGame = True     # Продолжается ли игра?
x = 0               # Число, которое вводит пользователь
startScore = 100    # Начальное количество очков
score = 0           # Текущее количество очков
maxScore = 0        # Максимальное количество очков
ret = 0             # Число, которое вввел пользователь в предыдущий раз
# =================================================================

# ----------Mainloop
while (playGame):
    digit = random.randint(lowDigit, hightDigit)
    print("Компьютер загадал число, попробуйте его отгадать!")
    countInput = 0 
    score = startScore
    
    # ------------- Внутренний цикл ------------
    while (not win and score > 0):
        print(f"заработано очков: {score}")
        print(f"рекорд: {maxScore}")
        
        x = ""
        while (not x.isdigit()):    # Пока в строке не число
            x = input(f"Введите число от {lowDigit} до {hightDigit}: ")
            if (not x.isdigit()):
                print("=" * 10 + " Введите, пожалуйста, число! " + "=" * 10)
                
        x = int(x)
        ret = x        
        
        if (x == digit):
            win = True
        else:
            length = abs(x - digit)
            if (length < 3):
                print("Очень горячо!")
            elif (length < 5):
                print("Горячо!")
            elif (length < 10):
                print("Тепло")
            elif (length < 15):
                print("Прохладно")
            elif (length < 20):
                print("Холодно")
            else:
                print("Ледяной ветер")
        
            if (countInput == 7):
                score -= 10
                if (digit % 2 == 0):
                    print("Число четное")
                else:
                    print("Число нечетное")
            elif (countInput == 6):
                score -= 8
                if (digit % 3 == 0):
                    print("Число делится на 3")
                else:
                    print("Число не делится на 3")
            elif (countInput == 5):
                score -= 4
                if (digit % 4 == 0):
                    print("Число делится на 4")
                else:
                    print("Число не делится на 4")
            elif (countInput > 2 and countInput < 5):
                score -= 2
                if (digit % 4 == 0):
                    print("Загаданное число МЕНЬШЕ ВАШЕГО")
                else:
                    print("Загаданное число БОЛЬШЕ ВАШЕГО")
            score -= 5
        countInput += 1
    
    if (x == digit):
            print(" ------------- Победа! Поздравляем! ------------- ")
            print(f"Вы закончили игру за количество ходов равное {countInput}")
    else:
        print("Ой, у вас закончились очки, вы проиграли")
        
    if (input("Enter - сыграть ещё, 0 - выход ") == "0"):
        playGame = False
    else:
        win = False
        
    if (score > maxScore):
        maxScore = score