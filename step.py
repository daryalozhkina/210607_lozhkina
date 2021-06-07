class Student:

    def __init__(self, name, birthday, address):
        self.name = name
        self.birthday = birthday
        self.address = address


class CollegeGroup:
    def __init__(self, name, student):
        self.name = name
        self.student = student