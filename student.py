class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def __str__(self):
        return f'{self.name} {self.age}'

    @staticmethod
    def parse(str):
        data = str.split(' ')
        if len(data) != 2:
            return Student('Parse Error', -1)
        return Student(data[0], int(data[1]))
