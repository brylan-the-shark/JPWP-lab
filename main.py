from service import Service
from student import Student
import menu

def catch_kb(func):
	def wrapper(*args, **kwargs):
		try:
			func(*args, **kwargs)
		except KeyboardInterrupt:
			pass
	
	return wrapper

@catch_kb
def input_student():
	sample = Student.invalid()
	keys: list[str] = [key for key in vars(sample).keys()]
	vals = [val for val in vars(sample).values()]
	ts: list[type] = [type(val) for val in vals]
	
	in_vals = [input(f'{key.capitalize()}: ') for key in keys]
	in_vals = [ts[i](val) for i, val in enumerate(in_vals)]

	s.add_student(Student(*in_vals))
	print('Added student to the database. Returning to main menu.')
	
	menu.pause()

@catch_kb
def list_students():
	for student in s.get_students():
		print(student)
	print('End of list. Returning to main menu.')
	
	menu.pause()

@catch_kb
def find_students():
	sample = Student.invalid()
	keys: list[str] = [key for key in vars(sample).keys()]
	vals = [val for val in vars(sample).values()]
	ts: list[type] = [type(val) for val in vals]

	i = menu.menu(*[f'By {key}' for key in keys])
	val = input(f'{keys[i].capitalize()}: ')
	val = ts[i](val)
	vals[i] = val
	Student(*vals)
	
	menu.clear()

	for student in s.find_students(**{keys[i]: val})[1]:
		print(student)
	print('End of list. Returning to main menu.')
	
	menu.pause()

@catch_kb
def remove_student():
	sample = Student.invalid()
	keys: list[str] = [key for key in vars(sample).keys()]
	vals = [val for val in vars(sample).values()]
	ts: list[type] = [type(val) for val in vals]
	
	i = menu.menu(*[f'Find by {key}' for key in keys])
	val = input(f'{keys[i].capitalize()}: ')
	val = ts[i](val)
	vals[i] = val
	Student(*vals)
	
	students = s.find_students(**{keys[i]: val})

	if len(students) == 1:
		idx = students[0][0]
	elif len(students) > 1:
		j = menu.menu(*[str(student[1]) for student in students])
		idx = students[j][0]
	else:
		raise KeyError('No students found')

	s.pop_student(idx)
	print('Removed student from the database. Returning to main menu.')
	
	menu.pause()

@catch_kb
def edit_student():
	sample = Student.invalid()
	keys: list[str] = [key for key in vars(sample).keys()]
	vals = [val for val in vars(sample).values()]
	ts: list[type] = [type(val) for val in vals]
	
	i = menu.menu(*[f'Find by {key}' for key in keys])
	val = input(f'{keys[i].capitalize()}: ')
	val = ts[i](val)
	vals[i] = val
	Student(*vals)
	
	students = s.find_students(**{keys[i]: val})

	if len(students) == 1:
		idx = students[0][0]
		new_value = students[0][1]
	elif len(students) > 1:
		j = menu.menu(*[str(student[1]) for student in students])
		idx = students[j][0]
		new_value = students[j][1]
	else:
		raise KeyError('No students found')
	
	print(f'Editing:\n{new_value}')
	menu.pause()

	while True:
		i = menu.menu(*([f'Edit {key}' for key in keys] + ['Done editing']))
		if i >= len(keys):
			break

		val = input(f'{keys[i].capitalize()}: ')
		val = ts[i](val)
		vals = [val for val in vars(new_value).values()]
		vals[i] = val

		try:
			new_value = Student(*vals)
		except Exception as e:
			menu.error(f'{e.__class__.__name__}: {e}')
			menu.pause()
	
	s.update_student(idx, new_value)
	print('Student updated. Returning to main menu.')
	
	menu.pause()

if __name__ == '__main__':
	try:
		menu.interactive_mode = menu.menu('Non-interactive mode (Other OSs)', 'Interactive mode (Windows)', msg='Choose non-interactive mode if interactive mode does not work for you')
		
		s = Service(int(input('Enter encryption key: ')))
	except Exception as e:
		menu.error(f'{e.__class__.__name__}: {e}')
		exit(1)
	except KeyboardInterrupt:
		exit(0)

	while True:
		try:
			match menu.menu('Add student', 'List students', 'Find students', 'Remove student', 'Update student', 'Exit'):
				case 0:
					input_student()
				case 1:
					list_students()
				case 2:
					find_students()
				case 3:
					remove_student()
				case 4:
					edit_student()
				case 5:
					break
		except Exception as e:
			menu.error(f'{e.__class__.__name__}: {e}')
			menu.pause()
		except KeyboardInterrupt:
			print('Aight dude')
			exit(0)
