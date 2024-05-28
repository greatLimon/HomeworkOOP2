        
class Mentor:
    def __init__(self, name:str, surname:str)->None:
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

 
class Lecturer(Mentor):
    def __init__(self, name:str, surname:str)->None:
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self)->str:
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__avrg_grade() :.1f}'

    # ==
    def __eq__(self, other)->bool:
        if isinstance(other, Lecturer):
            return self.__avrg_grade() == other.__avrg_grade()
        return False
    # <
    def __lt__(self, other)->bool:
        if isinstance(other, Lecturer):
            return self.__avrg_grade()<other.__avrg_grade()
        return False
    # >    
    def __gt__(self, other)->bool:
        if isinstance(other, Lecturer):
            return self.__avrg_grade()>other.__avrg_grade()
        return False
    # <=
    def __le__(self, other)->bool:
        return not self>other
    # >=
    def __ge__(self, other)->bool:
        return not self<other
    # !=
    def __ne__(self, other)->bool:
        return not self == other


    def __avrg_grade(self)->int:
        count = 0
        summary = 0
        for cource_grades_list in self.grades.values():
            count += len(cource_grades_list)
            summary += sum(cource_grades_list)
        if count != 0:
            return summary/count
        return 0

    

class Student:
    def __init__(self, name:str, surname:str, gender:str)->None:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def __str__(self)->str:
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__avrg_grade() :.1f}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}'
    
    # ==
    def __eq__(self, other)->bool:
        if isinstance(other, Student):
            return self.__avrg_grade() == other.__avrg_grade()
        return False
    # <
    def __lt__(self, other)->bool:
        if isinstance(other, Student):
            return self.__avrg_grade()<other.__avrg_grade()
        return False
    # >    
    def __gt__(self, other)->bool:
        if isinstance(other, Student):
            return self.__avrg_grade()>other.__avrg_grade()
        return False
    # <=
    def __le__(self, other)->bool:
        return not self>other
    # >=
    def __ge__(self, other)->bool:
        return not self<other
    # !=
    def __ne__(self, other)->bool:
        return not self == other


    def rate_lecturer(self, lecturer:Lecturer, course:str, grade:int):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        return f'Студент {self.name} {self.surname} поставил оценку {grade} лектору {lecturer.name} {lecturer.surname} на курсе {course}.'

    def __avrg_grade(self)->int:
        count = 0
        summary = 0
        for cource_grades_list in self.grades.values():
            count += len(cource_grades_list)
            summary += sum(cource_grades_list)
        if count != 0:
            return summary/count
        return 0 

class Reviewer(Mentor):

    def __str__(self)->str:
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student:Student, course:str, grade:int)->str:
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        return f'Эксперт {self.name} {self.surname} поставил оценку {grade} студенту {student.name} {student.surname} на курсе {course}.'

    




lect1 = Lecturer('Ivan', "Popov")
lect1.courses_attached.append('OOP')

lect2 = Lecturer('Maria', 'Andropova')
lect2.courses_attached.append('Git')

std1 = Student('Kirill', 'Mefodiy', 'Male')
std1.courses_in_progress.append('OOP')
std1.finished_courses.append('Git')
std1.rate_lecturer(lect1, 'OOP', 5)

rev1 = Reviewer('Anton', 'Cosolapov')
rev1.courses_attached.append('OOP')
rev1.rate_hw(std1, 'OOP', 9)

std2 = Student('Elena', 'ABC', 'Female')
std2.courses_in_progress.append('OOP')
std2.courses_in_progress.append('Git')
std2.rate_lecturer(lect1, 'OOP', 9)
std2.rate_lecturer(lect2,'Git',10)

rev1.rate_hw(std2, 'OOP', 9)

print(std1)
print('\n')
print(lect1)
print('\n')
print(rev1)
print('\n')
print(lect2)
print('\n')
print(std2)
print('\n')

print(std1 == std2)
print(std1 > std2)
print(std1 < std2)
print(std1 >= std2)
print(std1 <= std2)
print(std1 != std2)
print('\n')
print(lect1 == lect2)
print(lect1 > lect2)
print(lect1 < lect2)
print(lect1 >= lect2)
print(lect1 <= lect2)
print(lect1 != lect2)