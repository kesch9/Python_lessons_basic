# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib_list = [1]
    a = 1
    b = 1
    for _ in range (m - 1):
        a, b = b, a + b
        fib_list.append(a)
    return fib_list[fib_list.index(n):]

print(fibonacci(5, 6))
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    # Bubble sort
    n = len(origin_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
    return origin_list

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(filter_func, iter):
    new_iter = []
    for i in iter:
        if filter_func(i):
            new_iter.append(i)
    return new_iter

print(list(my_filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
#       A2__________A4
#      /            /
#     /            /
#    A1___________A3

def parallelogram (a1,a2,a3,a4):
    if a2[0] - a1[0] == a4[0] - a3[0] and a2[1] - a1[1] == a4[1] - a3[1]:
        return True
    return False

print(parallelogram([0,0],[2,2],[6,0],[8,2]))
print(parallelogram([0,0],[2,2],[6,0],[8,23]))