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
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rate()}'


class Reviewer(Mentor):

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

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
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rate()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def average_rate(self):
        course_grades = []
        for grade in self.grades:
            course_grades.append(sum(self.grades[grade]) / len(self.grades[grade]))
        if course_grades:
            return round(sum(course_grades) / len(course_grades), 1)
        return 0

    def rate_lecture(self, lecturer, course, rate):
        if isinstance(lecturer, Reviewer):
            return 'Ошибка'

        if course not in lecturer.courses_attached:
            return 'Ошибка'

        if rate > 10 or rate < 1:
            return 'Ошибка'

        lecturer.grades.setdefault(course, []).append(rate)


def average_students(students , course):
    result = []
    for student in students:
        if course in student.grades:
            result.append(round(sum(student.grades[course]) / len(student.grades[course]), 1))
    if result:
        return round(sum(result) / len(result), 1)
    return 0


def average_lectures(lectures , course):
    result = []
    for lecture in lectures:
        if course in lecture.grades:
            result.append(round(sum(lecture.grades[course]) / len(lecture.grades[course]), 1))
    if result:
        return round(sum(result) / len(result), 1)
    return 0


reviewer = Reviewer("My", "Gof")
reviewer.courses_attached.append('Python')
reviewer.courses_attached.append('Java')
reviewer.courses_attached.append('C++')
print(reviewer)


student_1 = Student("Max", "Pain", "M")
student_2 = Student("Neo", "Neo", "M")

lecturer_1 = Lecturer("Torr", "Torr")
lecturer_2 = Lecturer("Halk", "Bruce")

lecturer_1.courses_attached.append('Python')
lecturer_2.courses_attached.append('Python')
lecturer_1.courses_attached.append('Java')
lecturer_2.courses_attached.append('Java')
lecturer_1.courses_attached.append('C++')
lecturer_2.courses_attached.append('C++')

student_1.courses_in_progress.append('Python')
student_1.courses_in_progress.append('Java')
student_1.courses_in_progress.append('C++')

student_2.courses_in_progress.append('Python')
student_2.courses_in_progress.append('Java')
student_2.courses_in_progress.append('C++')

reviewer.rate_hw(student_1, "Python", 5)
reviewer.rate_hw(student_1, "Java", 6)
reviewer.rate_hw(student_1, "C++", 7)
reviewer.rate_hw(student_2, "Python", 6)
reviewer.rate_hw(student_2, "Java", 7)
reviewer.rate_hw(student_2, "C++", 8)

# ошибки
print(reviewer.rate_hw(student_1, "Delphi", 5))
print(reviewer.rate_hw(student_2, "1C", 5))


print(student_1)
print(average_students([student_1, student_2], "Python"))
print(student_1 == student_2)

student_1.rate_lecture(lecturer_1, "Python", 4)
student_1.rate_lecture(lecturer_1, "Java", 4)
student_1.rate_lecture(lecturer_1, "C++", 4)
student_1.rate_lecture(lecturer_2, "Python", 5)
student_1.rate_lecture(lecturer_2, "Java", 5)
student_1.rate_lecture(lecturer_2, "C++", 5)

# ошибки
print(student_1.rate_lecture(lecturer_1, "1C", 6))
print(student_2.rate_lecture(lecturer_2, "Delphi", 3))
print(student_2.rate_lecture(lecturer_2, "Delphi", 11))
###############################################################

student_2.rate_lecture(lecturer_1, "Python", 8)
student_2.rate_lecture(lecturer_1, "Java", 8)
student_2.rate_lecture(lecturer_1, "C++", 8)
student_2.rate_lecture(lecturer_2, "Python", 8)
student_2.rate_lecture(lecturer_2, "Java", 8)
student_2.rate_lecture(lecturer_2, "C++", 8)


print(student_2.rate_lecture(reviewer, "C++", 8))


print(lecturer_1)
print(average_students([lecturer_1, lecturer_2], "Python"))
