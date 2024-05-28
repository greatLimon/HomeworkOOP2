        
class Mentor:
    def __init__(self, name:str, surname:str)->None:
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

 
class Lecturer(Mentor):
    def __init__(self, name:str, surname:str)->None:
        super().__init__(name, surname)
        self.grades = {}

class Student:
    def __init__(self, name:str, surname:str, gender:str)->None:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer:Lecturer, course:str, grade:int):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        return f'Студент {self.name} {self.surname} поставил оценку {grade} лектору {lecturer.name} {lecturer.surname} на курсе {course}.'

class Reviewer(Mentor):

    def rate_hw(self, student:Student, course:str, grade:int)->str:
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        return f'Эксперт {self.name} {self.surname} поставил оценку {grade} студенту {student.name} {student.surname} на курсе {course}.'

