# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
testLst = [2, -5, 8, 9, -25, 25, 4]
newLst = []
for i in testLst:
    if i >= 0 and (i ** 0.5).is_integer():
        newLst.append(int(i ** 0.5))
print(newLst)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
testDate = '02.11.2013';
day = int (testDate[:2])
mon = int (testDate[3:5])

day_dict = {1:'первое', 2 :'второе', 3 : 'третье', 4 : 'четвертое', 5 : 'пятое', 6 : 'шестое',
            7 : 'седьмое', 8 : 'восьмое', 9 : 'девятое', 10 : 'десятое', 11 : 'одиннадцатое', 12 : 'двенадцатое',
            13 : 'тринадцатое', 14 : 'четырнадцатое', 15 : 'пятнадцатое', 16 : 'шестнадцатое', 17 : 'семнадцатое',
            18 : 'восемнадцатое', 19 : 'девятнадцатое', 20 : 'двацвадцатое', 21 : 'двацвадцать первое',
            22 : 'двацвадцать второе', 23 : 'двацвадцать третье', 24 : 'двацвадцать четвертое',
            25 : 'двацвадцать пятое', 26 : 'двацвадцать шестое', 27 : 'двацвадцать седьмое', 28 : 'двацвадцать восьмое',
            29 : 'двацвадцать девятое', 30 : 'тридцатое', 31 : 'тридцать первое',}

month_dict = { 1 : 'января', 2 : 'февраля', 3 : 'марта', 4 : 'апреля', 5 : 'мая', 6 : 'июня', 7 : 'июля', 8 : 'августа',
          9 : 'сентября', 10 : 'октября', 11 : 'ноября', 12 : 'декабря'}
print('{} {} {} года'.format(day_dict[day], month_dict[mon],testDate[6:]))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
n = 10
testLst = [random.randint(-100, 100) for _ in range(n)]
print(testLst)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
lst1 = [1, 2, 4, 5, 6, 2, 5, 2]
lstSet = list(set(lst1))
print(lstSet)
lst1 = [1 , 2, 4, 5, 6, 2, 5, 2]
lst2 = [i for i in lst1 if lst1.count(i) == 1]
print(lst2)
