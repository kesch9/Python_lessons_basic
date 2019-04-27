#!/usr/bin/python3
"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Cards:

    def __init__(self, name_cards, list_value):
        self.name_cards = name_cards
        self.listValue = list_value

    def __str__(self):
        list_value_str = ""
        for row in self.listValue:
            list_value_str += ' '.join([str(elem) for elem in row])
            list_value_str += '\n'
        return f"{self.name_cards}\n" \
               f"{list_value_str}" \
               f"--------------------------"

    def del_val(self, val):
        for row in self.listValue:
            if val in row:
                row[row.index(val)] = ' '
                return True
        return False

    def win(self):
        for row in self.listValue:
            for val in row:
                if ' ' != val:
                    return False
        return True

def gen_cards():
    cards = []
    for i in range(3):
        cards.append([])
        for j in range(9):
            cards[i].append(' ')
    i = 0
    val = [i for i in range(91)]
    while ( i < 15):
        a = random.randint(0, 2)
        b = random.randint(0, 8)
        if cards[a][b] == ' ':
            k = random.randint(0, len(val))
            cards[a][b] = val[k]
            val.remove(val[k])
            i += 1
    return cards

listComp = gen_cards()
listUser = gen_cards()
name = "------ Ваша карточка -----"
cardsUser = Cards(name, listUser)
name = "-- Карточка компьютера ---"
cardsComp = Cards(name, listComp)
print("---ИГРА НАЧИНАЕТСЯ---")
keg = [i for i in range(91)]

while(True):
    ind = random.randint(0, len(keg))
    print(f"Новый бочонок: {keg[ind]} (осталось {len(keg)-1})")
    elem = keg[ind]
    keg.remove(elem)
    print(cardsUser)
    print(cardsComp)
    choise_user = input("Зачеркнуть цифру? (y/n) ")
    if choise_user == "y":
        if not cardsUser.del_val(elem):
            print("Вы проиграли и игра завершена")
            break
    else:
        if cardsUser.del_val(elem):
            print("Вы проиграли и игра завершена")
            break
    cardsComp.del_val(elem)
    if cardsUser.win():
        print("Вы выиграли !!!!")
        break




