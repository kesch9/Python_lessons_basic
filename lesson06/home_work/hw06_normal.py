# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Clazz:
    def __init__(self,name,students=[]):
        self.name = name
        self.__students = students

    def get_students(self):
        return self.__students
    def add_students(self,Student):
        self.__students.append(Student)
    def remove_student(self,Student):
        if Student in self.__student:
            self.__students.remove(Student)

class Student:
    def __init__(self,name,father,mother):
        self.name = name
        self.father = father
        self.mother = mother


class Teacher:
    def __init__(self, name, course, classes=[]):
        self.name = name
        self.__classes = classes
        self.course = course

    def get_classes(self):
        return self.__classes

    def add_classes(self, classes):
         self.__classes.append(classes)

    def remove_student(self, classes):
        if classes in self.__student:
                self.__classes.remove(classes)

class Course:
    def __init__(self,name):
        self.name = name

class Father:
    def __init__(self,name):
        self.name = name

class Mother:
    def __init__(self,name):
        self.name = name

class School:
    def __init__(self,name,classes = []):
        self.name = name
        self.__classes = classes
    def get_classes(self):
        return self.__classes

    def add_classes(self, classes):
         self.__classes.append(classes)

    def remove_student(self, classes):
        if classes in self.__student:
                self.__classes.remove(classes)

if __name__ == '__main__':
    father = Father('Petr')
    mother = Mother('Katya')
    student = Student('Ivan',father,mother)
    course = Course('Mathematika')
    clazz = Clazz('5A',[student])
    teacher = Teacher('Teach',course,[clazz])
    school = School('Best',[clazz])
