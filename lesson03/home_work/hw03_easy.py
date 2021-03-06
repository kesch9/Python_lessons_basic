# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    s = "%0." + str(ndigits) + "f"
    return s % number
    # round(number,ndigits)
    # return (int(number * 10 ** ndigits)) / 10 ** ndigits


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
     str_number = str(ticket_number)
     if len(str_number) == 6:
         a = int(str_number[0]) + int(str_number[1]) + int(str_number[2])
         b = int(str_number[3]) + int(str_number[4]) + int(str_number[5])
         return a == b


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
