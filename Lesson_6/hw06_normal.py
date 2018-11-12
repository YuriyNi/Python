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

class person:
   def __init__(self, name, surname, L_name):
       self._name = name
       self._surname = surname
       self._L_name = L_name

       @property
       def full_name(self):
           return " {}{} {}".format(self.name, self.surname, self.L_name)


class subject:
    def __init__(self, name):
        self.name = name


class teacher(person):
    def __init__(self, name, surname, L_name, subject):
        person.__init__(self, name, surname, L_name)
        self.subject = subject

class student (person):
    def __init__(self, name, surname, L_name, mother, father):
        person.__init__(self, name, surname, L_name)
        self.mother = mother
        self.father = father

    def get_parents(self):
        return [self.mother.full_name, self.father.full_name]

class Class:
    def __init__(self, number, char):
        self.number = number
        self.char = char
        self.teachers = []
        self.students = []

    @property
    def name (self):
        return "{}{} {}".format(self.number, self.char)

    def add_teacher (self, *args):
        for a in args:
            self.teachers.append(a)

    def add_student (self, *args):
        for a in args:
            self.students.append(a)


class School:
    def __init__(self):
        self.classes = []      #список классов

    def add_classes (self, *args):
        for a in args
            self.classes.append(a)

# создаем метод вывести список классов
    def get_classes (self):
        return [x.name for x in self.classes]

# создаем метод вывести список учеников
    def get_students (self, classname):
        students = [x.students for x in self.classes if x.name == classname]
        return [el.full_name for x in classes[0].teacher]

# создаем метод получить предметов для ученика
    def get_subjects (self, studentname):
        classes = [x for x in self.classes if studentname in [y.full_name for y in x.students]]
        return [x.subject.name for x in classes[0].teachers]

# создаем метод получить родителей
    def get_parents (self, studentname):
        # Список всех учеников в классе выбранного ученика
        class_students = [x.students for x in self.classes if studentname in [y.full_name for y in x.students]]

        #доступ к выбранному ученику
        students = [x for x in class_students[0] if studentname == x.full_name]
        #доступ к его родителям
        return students[0].get_parents()
    def get_teachers (self, classname):
        teachers = [ x.teachers for x in self.classes if x.name == classname]
        return [x.full_name for x in teachers[0]]













#Children = person()



