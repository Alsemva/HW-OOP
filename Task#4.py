class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached\
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grades(self):
        sum_grades = 0
        counter = 0
        for item in self.grades.values():
            sum_grades += sum(item)
            counter += len(item)
        average = round(sum_grades / counter, 1)
        return average

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_grades()}\
        \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\
        \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            return print("Not a Student")
        return self._average_grades() < other._average_grades()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return print("Not a Student")
        return self._average_grades() == other._average_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grades(self):
        sum_grades = 0
        counter = 0
        for item in self.grades.values():
            sum_grades += sum(item)
            counter += len(item)
        average = round(sum_grades / counter, 1)
        return average

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grades()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return print("Not a Lecturer")
        return self._average_grades() < other._average_grades()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return print("Not a Lecturer")
        return self._average_grades() == other._average_grades()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def average_grades_all_students(students_list, course):
    counter = 0
    sum_grades = 0
    for student in students_list:
        if course in student.grades:
            counter += len(student.grades[course])
            sum_grades += sum(student.grades[course])
    average = round(sum_grades / counter, 1)
    return average


def average_grades_all_lecturers(lecturers_list, course):
    counter = 0
    sum_grades = 0
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            counter += len(lecturer.grades[course])
            sum_grades += sum(lecturer.grades[course])
    average = round(sum_grades / counter, 1)
    return average


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Front-end', 'Git']
best_student.finished_courses += ['Введение в программирование']

best_student_2= Student('Igor', 'Knyaz', 'male')
best_student_2.courses_in_progress += ['Python', 'C++', 'Git']
best_student_2.finished_courses += ['Введение в программирование', 'Английский в IT']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer_2 = Reviewer('Sim', 'Bud')
cool_reviewer_2.courses_attached += ['C++']

cool_lecturer = Lecturer('Ivan', 'Petrov')
cool_lecturer.courses_attached += ['Python']

cool_lecturer_2 = Lecturer('Entony', 'Stone')
cool_lecturer_2.courses_attached += ['Python']

best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 9)
best_student.rate_hw(cool_lecturer, 'Python', 10)

best_student.rate_hw(cool_lecturer_2, 'Python', 10)
best_student.rate_hw(cool_lecturer_2, 'Python', 8)
best_student.rate_hw(cool_lecturer_2, 'Python', 10)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer_2.rate_hw(best_student_2, 'C++', 10)
cool_reviewer_2.rate_hw(best_student_2, 'C++', 7)
cool_reviewer_2.rate_hw(best_student_2, 'C++', 10)
cool_reviewer.rate_hw(best_student_2, 'Python', 10)
cool_reviewer.rate_hw(best_student_2, 'Python', 10)

print(cool_reviewer, '\n')
print(cool_reviewer_2, '\n')

print(cool_lecturer, '\n')
print(cool_lecturer_2, '\n')

print(best_student, '\n')
print(best_student_2, '\n')

print(cool_lecturer > cool_lecturer_2)
print(cool_lecturer == cool_lecturer_2)
print(best_student < best_student_2)
print(best_student != best_student_2)

students_list = [best_student, best_student_2]
print(f"Средняя оценка по всем студентам: {average_grades_all_students(students_list, 'Python')}")

lecturers_list = [cool_lecturer, cool_lecturer_2]
print(f"Средняя оценка по всем лекторам: {average_grades_all_lecturers(lecturers_list, 'Python')}")
