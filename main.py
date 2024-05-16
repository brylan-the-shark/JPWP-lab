from service import Service
from student import Student

if __name__ == '__main__':
    try:
        s = Service()
        s.add_student(Student('Krzysztof', 20))
        s.add_student(Student('Janusz', 40))

        students = s.get_students()
        for current in students:
            print(current)
    except IOError as e:
        print(f'An error occurred: {e}')
