# Задание № 3. Полиморфизм и магические методы

### Перегрузите магический метод __str__ у всех классов:

для экономии строк создал обособленную функцию подсчета рейтинга оценок
```python
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
```

далее создал общий класс для всех участников образовательного процесса и перегрузил в нем магические методы __str__ и __lt__
```python
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
```