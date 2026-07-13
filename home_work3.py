
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


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
        self.grades = {}

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
