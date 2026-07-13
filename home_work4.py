
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {'python': [3,4], 'java': [6,7,8], 'c++': [9,10,11]}


class Lecturer(Mentor):

    def average_rate(self):
        course_grades = []
        for grade in self.grades:
            course_grades.append(sum(self.grades[grade]) / len(self.grades[grade]))
        if course_grades:
            return round(sum(course_grades) / len(course_grades), 1)
        return 0

    def __eq__(self, other):
        return bool(self.average_rate() == other.average_rate())

    def __gt__(self, other):
        return bool(self.average_rate() > other.average_rate())

    def __lt__(self, other):
        return bool(self.average_rate() < other.average_rate())

    def __str__(self):
        return f'Имя: {self.surname}\nФамилия: {self.name}\nСредняя оценка за лекции: {self.average_rate()}'


class Reviewer(Mentor):

    def __str__(self):
        return f'Имя: {self.surname}\nФамилия: {self.name}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {'python': [3,4], 'java': [6,7,8], 'c++': [9,10,11]}

    def __eq__(self, other):
        return bool(self.average_rate() == other.average_rate())

    def __gt__(self, other):
        return bool(self.average_rate() > other.average_rate())

    def __lt__(self, other):
        return bool(self.average_rate() < other.average_rate())

    def __str__(self):
        return (f'Имя: {self.surname}\nФамилия: {self.name}\nСредняя оценка за домашние задания: {self.average_rate()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def average_rate(self):
        course_grades = []
        for grade in self.grades:
            course_grades.append(sum(self.grades[grade]) / len(self.grades[grade]))
        if course_grades:
            return round(sum(course_grades) / len(course_grades), 1)
        return 0

    @staticmethod
    def rate_lecture(lecturer, course, rate):
        if isinstance(lecturer, Reviewer):
            return 'Ошибка'

        if course not in lecturer.courses_attached:
            return 'Ошибка'

        if rate > 10 or rate < 1:
            return 'Ошибка'

        lecturer.grades.setdefault(course, []).append(rate)


def compare_students(students , course):
    compare_result = []

    for grade in student1.grades:
        if grade in student2.grades:
            average_course1 = round(sum(student1.grades[grade]) / len(student1.grades[grade]), 1)
            average_course2 = round(sum(student2.grades[grade]) / len(student2.grades[grade]), 1)
            if average_course1 > average_course2:
                mess = f'По курсу {grade} студент {student1.name} занимается лучше студента {student2.name}'
            elif average_course2 > average_course1:
                mess = f'По курсу {grade} студент {student2.name} занимается лучше студента {student1.name}'
            else:
                mess = f'По курсу {grade} студенты {student2.name}, {student1.name} одинаково хорошо занимаются'
            compare_result.append(mess)
    return compare_result


def compare_lectures(lecture1, lecture2):
    compare_result = []
    # имеет смысл сравнивать только совпдающие курсы
    for grade in lecture1.grades:
        if grade in lecture2.grades:
            average_course1 = round(sum(lecture1.grades[grade]) / len(lecture1.grades[grade]), 1)
            average_course2 = round(sum(lecture2.grades[grade]) / len(lecture2.grades[grade]), 1)
            if average_course1 > average_course2:
                mess = f'По курсу {grade} лектор {lecture1.name} преподает лучше лектора {lecture2.name}'
            elif average_course2 > average_course1:
                mess = f'По курсу {grade} лектор {lecture2.name} преподает лучше лектора {lecture1.name}'
            else:
                mess = f'По курсу {grade} лекторы {lecture2.name}, {lecture1.name} одинаково хорошо преподают'
            compare_result.append(mess)
    return compare_result


