from service import Service
from student import Student
from menu import pause, clear
import menu

def input_student():
	sample = Student.invalid()
	keys : list[str] = [key for key in vars(sample).keys()]
	ts : list[type] = [type(val) for val in vars(sample).values()]
	vals = [input(f'{key.capitalize()}: ') for key in keys]
	vals = [ts[i](val) for i, val in enumerate(vals)]

	s.add_student(Student(*vals))
	print('Added student to the database. Returning to main menu.')
	
	pause()

def list_students():
	for student in s.get_students():
		print(student)
	print('End of list. Returning to main menu.')
	
	pause()

def find_students():
	sample = Student.invalid()
	keys : list[str] = [key for key in vars(sample).keys()]
	i = menu.menu(*[f'By {key}' for key in keys])
	val = input(f'{keys[i].capitalize()}: ')
	t = type(vars(sample)[keys[i]])
	val = t(val)
	vals = [val for val in vars(sample).values()]
	vals[i] = val
	Student(*vals)
	
	clear()

	for student in s.find_students(**{keys[i]: val}):
		print(student)
	print('End of list. Returning to main menu.')
	
	pause()

def remove_student():
	students = s.get_students()
	idx = menu.menu(*[str(student) for student in students], 'Cancel')
	if idx >= len(students):
		return

	s.remove_student(idx)
	print('Removed student from the database. Returning to main menu.')
	
	pause()

if __name__ == '__main__':
	menu.interactive_mode = menu.menu('Non-interactive mode (nubmers for navigation)', 'Interactive mode (arrow keys for navigation)', msg='Choose non-interactive mode if interactive mode does not work for you')

	try:
		s = Service(int(input('Enter encryption key: ')))
	except Exception as e:
		print(f'An error occurred: {e}')
		exit(1)

	while True:
		try:
			match menu.menu('Add student', 'List students', 'Find students', 'Remove student', 'Exit'):
				case 0:
					input_student()
				case 1:
					list_students()
				case 2:
					find_students()
				case 3:
					remove_student()
				case 4:
					exit()
		except Exception as e:
			print(f'{e.__class__.__name__}: {e}')
			pause()
