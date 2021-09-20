class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grading_lecturer(self, lecturer, course, grade):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            if int(grade) >= 1 and int(grade) <= 10:
                if hasattr(lecturer, 'grades'):
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades = {course: [grade]}
            else:
                print(f"{grade} - для оценки введите число от 1 до 10")
        else:
            if course not in lecturer.courses_attached:
                print(f"{lecturer.name} {lecturer.surname} не закреплен за курсом!")
        
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def grading(self, student, course, grade):
        if int(grade) >= 1 and int(grade) <= 10:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            print(f"{grade} - для оценки введите число от 1 до 10")


