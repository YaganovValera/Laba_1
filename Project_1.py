import random

name = input("Введите ваше имя: ")
name = name.title()
print(f"{name} хотите сыграть в игру?")
while(True):
    answer = input("""Введите "да" или "нет": """)
    if(answer == "да"): print("Отлично!!!"); break
    elif(answer == "нет"):
        print("Очень жаль. До свидания")
        answer = False
        break
    else: print("Некорректный ввод.")
if (answer == False): exit(0)
print("""\tИнструкция по игре: \n1) Суть игры: Я загадываю число от 1 до 100(включительно), а вы пытаетесь его отгадать.
2) Если вы хотите начать сначала, то введите "replay"
3) Если вы хотите закончить игру, то введите "stop".
\tЕсли все понятно, то давайте начнем.""")

def play():
    game_end = False
    while(True):
        number = random.randint(1, 101)
        while(True):
            answer = input("Введите число от 1 до 100: ")
            if(answer == "stop"): game_end = True; break
            elif(answer == "replay"): break
            elif(answer.isdigit() and int(answer) >= 1 and int(answer) <= 100):
                if(int(answer) < number):
                    print("Загаданное число больше.")
                if (int(answer) > number):
                    print("Загаданное число меньше.")
                if (int(answer) == number):
                    print("Поздравляю вы победили!!!"
                          "Давайте сыграем ещё раз.")
                    break
            elif(answer.isdigit() and (int(answer) < 1 or int(answer) > 100)):
                print("Число не входит в диапазон от 1 до 100")
            else:
                print("Некорректный ввод.")
        if(game_end == True): print("Очень жаль, что вы уходите. До свидания."); break
play()