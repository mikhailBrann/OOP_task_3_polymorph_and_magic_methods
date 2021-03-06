# для экономии строк обособленная функция считает рейтинг оценок
def calculate_rating(course_list):
    total_points = 0
    total_length = 0
    # проверяем аттрибут на пустоту
    if bool(course_list):
        for course_val in course_list.values():
            total_points += sum(list(course_val))
            total_length += len(list(course_val))
        return round(total_points / total_length, 1)
    else:
        return 0.0


class Person:
    def __str__(self):
        this_class_name = self.__class__.__name__

        if this_class_name == 'Reviewer':
            result = f"Имя: {self.name}\nФамилия: {self.surname}\n"

        elif this_class_name == 'Lecturer':
            result = f"Имя: {self.name}\nФамилия: {self.surname}"
            average_rating = calculate_rating(self.grades)
            result += f"\nСредняя оценка за лекции: {average_rating}\n"

        elif this_class_name == 'Student':
            result = f"Имя: {self.name}\nФамилия: {self.surname}"
            average_rating = calculate_rating(self.grades)
            result += f"\nСредняя оценка за домашние задания: {average_rating}"

            if len(self.courses_in_progress) > 0:
                courses_name_list = ','.join(self.courses_in_progress)
                result += f"\nКурсы в процессе изучения: {courses_name_list}"
            else:
                result += f"\nКурсы в процессе изучения: пока нет"

            if len(self.finished_courses) > 0:
                courses_name_list = ','.join(self.finished_courses)
                result += f"\nЗавершенные курсы: {courses_name_list}"
            else:
                result += f"\nЗавершенные курсы: пока нет"
            result += '\n'
            
        return result

    def __lt__(self, other):
        this_class_name = self.__class__.__name__

        if this_class_name == 'Student' or this_class_name == 'Lecturer':
            return calculate_rating(self.grades) < calculate_rating(other.grades)


class Student(Person):
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
                if course in lecturer.grades:
                    lecturer.grades[course].append(grade)
                else:
                    lecturer.grades.setdefault(course, [grade])
            else:
                print(f"{grade} - для оценки введите число от 1 до 10")
        else:
            if course not in lecturer.courses_attached:
                print(f"{lecturer.name} {lecturer.surname} не закреплен за курсом!")
        
        
class Mentor(Person):
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
        self.grades = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def grading(self, student, course, grade):
        if int(grade) >= 1 and int(grade) <= 10:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades.setdefault(course, [grade])
        else:
            print(f"{grade} - для оценки введите число от 1 до 10")


student_lexa = Student('Alex', 'Alekseev', 'Male')
student_inna = Student('Inna', 'Innova', 'Female')

student_lexa.courses_in_progress.append('Git')
student_inna.courses_in_progress.append('Git')
student_lexa.courses_in_progress.append('Python')
student_inna.courses_in_progress.append('Python')


new_lacturer = Lecturer('Ivan', 'Ivanov')

new_lacturer.courses_attached.append('Git')
new_lacturer.courses_attached.append('Python')

student_lexa.grading_lecturer(new_lacturer, 'Git', 8)
student_inna.grading_lecturer(new_lacturer, 'Git', 7)
student_lexa.grading_lecturer(new_lacturer, 'Python', 9)
student_inna.grading_lecturer(new_lacturer, 'Python', 8)


new_reviewer = Reviewer('Igor', 'Igorev')

new_reviewer.grading(student_lexa, 'Git', 7)
new_reviewer.grading(student_lexa, 'Python', 8)
new_reviewer.grading(student_inna, 'Git', 8)
new_reviewer.grading(student_inna, 'Python', 7)

student_lexa.finished_courses.append('PHP')


print(new_lacturer)
print(new_reviewer)
print(student_lexa)
print(student_inna)

print(student_lexa < new_lacturer)
print(new_lacturer < student_lexa)