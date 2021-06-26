class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectures(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rating:
                lecturer.rating[course] += [rate]
            else:
                lecturer.rating[course] = [rate]
        else:
            return 'Ошибка'

    def grades_average(self):
        grades_all = []
        for grade in self.grades.values():
            grades_all += grade
        grade_average = sum(grades_all) / len(grades_all)
        return '{0:.1f}'.format(grade_average)

    def __str__(self):
        return (f'Имя студента: {self.name} \nФамилия студента: {self.surname}'
                f'\nСредняя оценка за домашние задания: {self.grades_average()}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершённые курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        else:
            if self.grades_average() < other.grades_average():
                return f'Студент {other.name} учится лучше, чем студент {self.name}'
            else:
                return f'Студент {self.name} учится лучше, чем студент {other.name}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        res = f'Имя проверяющего: {self.name} \nФамилия проверяющего: {self.surname}\n'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating = {}

    def rates_average(self):
        rates_all = []
        for rate in self.rating.values():
            rates_all += rate
        rate_average = sum(rates_all) / len(rates_all)
        return '{0:.1f}'.format(rate_average)

    def __str__(self):
        res = f'Имя лектора: {self.name} \nФамилия лектора: {self.surname} \nСредняя оценка за лекции: {self.rates_average()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        else:
            if self.rates_average() < other.rates_average():
                return f'У лектора {other.name} рейтинг лучше, чем у лектора {self.name}'
            else:
                return f'У лектора {self.name} рейтинг лучше, чем у лектора {other.name}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_one = Student('Mary', 'Jane', 'female')
student_one.courses_in_progress += ['Python', 'Git', 'Java']
student_one.finished_courses += ['Android']

student_two = Student('Leo', 'Mackwin', 'male')
student_two.courses_in_progress += ['Python', 'Git', 'Java']
student_two.finished_courses += ['Devops']

reviewer_one = Reviewer('Kate', 'Middleton')
reviewer_one.courses_attached += ['Python', 'Git', 'Java']

reviewer_two = Reviewer('Mark', 'Sloan')
reviewer_two.courses_attached += ['Python', 'Java', 'Git']

lecturer_one = Lecturer('Meredith', 'Gray')
lecturer_one.courses_attached += ['Python', 'Git', 'Java']

lecturer_two = Lecturer('Derek', 'Shepard')
lecturer_two.courses_attached += ['Java', 'Python', 'Git']

student_one.rate_lectures(lecturer_one, 'Python', 9)
student_one.rate_lectures(lecturer_one, 'Git', 5)
student_one.rate_lectures(lecturer_two, 'Java', 6)
student_two.rate_lectures(lecturer_one, 'Python', 10)
student_two.rate_lectures(lecturer_one, 'Git', 9)
student_two.rate_lectures(lecturer_two, 'Java', 10)
student_two.rate_lectures(lecturer_two, 'Python', 6.5)
student_two.rate_lectures(lecturer_two, 'Git', 10)
student_one.rate_lectures(lecturer_two, 'Python', 7)


reviewer_one.rate_hw(student_two, 'Python', 10)
reviewer_one.rate_hw(student_two, 'Git', 9)
reviewer_two.rate_hw(student_one, 'Python', 7)
reviewer_one.rate_hw(student_two, 'Git', 5)
reviewer_two.rate_hw(student_one, 'Python', 6)
reviewer_two.rate_hw(student_one, 'Java', 10)
reviewer_one.rate_hw(student_one, 'Java', 8)
reviewer_one.rate_hw(student_two, 'Java', 6)
reviewer_one.rate_hw(student_one, 'Git', 8)


print(student_two)
print(student_one)
print(reviewer_two)
print(reviewer_one)
print(lecturer_one)
print(lecturer_two)


def average_all_grades(students_list, course):
    course_list = []
    for student in students_list:
        if course in student.grades.keys():
            course_list += student.grades[course]
    res = sum(course_list) / len(course_list)
    return 'Средняя оценка всех студентов за домашние задания: {0:.1f}'.format(res)

def average_all_rates(lecturer_list, course):
    rate_list = []
    for lecturer in lecturer_list:
        if course in lecturer.rating.keys():
            rate_list += lecturer.rating[course]
    res = sum(rate_list) / len(rate_list)
    return 'Средняя оценка всех лекторов за лекции курса: {0:.1f}'.format(res)

print(average_all_grades([student_one, student_two], 'Python'))
print(average_all_rates([lecturer_two, lecturer_one], 'Python'))

