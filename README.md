# Задание № 2. Атрибуты и взаимодействие классов.
В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания. 
Теперь это могут делать только Reviewer (реализуйте такой метод):

```python
def grading(self, student, course, grade):
    if int(grade) >= 1 and int(grade) <= 10:
        if course in student.grades:
            student.grades[course].append(grade)
        else:
            student.grades[course] = [grade]
    else:
        print(f"{grade} - для оценки введите число от 1 до 10")
```


А что могут делать лекторы? Получать оценки за лекции от студентов :) 
Реализуйте метод выставления оценок лекторам у класса Student (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer, в котором ключи – названия курсов, а значения – списки оценок). Лектор при этом должен быть закреплен за тем курсом, на который записан студент:

```python
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
```