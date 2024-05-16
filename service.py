from student import Student

class Service:
    def add_student(self, student):
        with open('db.txt', 'a') as file:
            file.write(f'{student}\n')

    def get_students(self):
        ret = []
        with open('db.txt', 'r') as file:
            for line in file:
                ret.append(Student.parse(line.strip()))
        return ret

    def find_student_by_name(self, name):
        return None
