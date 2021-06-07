class Student:
    def __init__(self, name, birthday, address):
        self.name = name
        self.birthday = birthday
        self.address = address


class CollegeGroup:
    def __init__(self, name):
        self.name = name
        self.students = []



student_1 = Student('Иванов Иван Иванович', '10.07.2004', 'г. Курган, ул. Ленина')
student_2 = Student('Петров Петр Петрович', '07.11.2003', 'г. Курган, ул. Карельцева')
group_1 = CollegeGroup('ИТ-33')
group_1.__add__(student_1)
group_1._add_(student_2)