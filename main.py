from service import Service
from student import Student
from menu import menu, pause

def input_student():
	try:
		s.add_student(Student(input('Name: '), int(input('Age: ')), input('Birthday: ')))
		print('Added student to the database. Returning to main menu.')
	except Exception as e:
		print(f'An error occurred: {e}')
	pause()

def list_students():
	try:
		for student in s.get_students():
			print(student)
		print('End of list. Returning to main menu.')
	except Exception as e:
		print(f'An error occurred: {e}')
	pause()

if __name__ == '__main__':
	try:
		s = Service()
		
		while True:
			match menu('Add studend', 'List students'):
				case 0:
					input_student()
				case 1:
					list_students()
	except IOError as e:
		print(f'An error occurred: {e}')
