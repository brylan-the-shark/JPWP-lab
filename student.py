import re

class Student:
	name : str
	surname : str
	age : int
	birthday : str

	def __init__(self, name, surname, age, birthday):
		if not re.fullmatch('[A-Z][a-z]*', name):
			raise ValueError('Name must only contain letters and be capitalized')
		if not re.fullmatch('[A-Z][a-z]*', surname):
			raise ValueError('Surame must only contain letters and be capitalized')
		if age < 0 or age > 150:
			raise ValueError('Age must be in range 0 to 150')
		if not re.fullmatch('\d{2}-\d{2}-\d{4}', birthday):
			raise ValueError('Birthday must be in DD-MM-YYYY format')

		self.name = name
		self.surname = surname
		self.age = age
		self.birthday = birthday

	def __str__(self):
		return '\t'.join(str(v) for v in vars(self).values())

	@staticmethod
	def parse(str):
		data = str.split('\t')

		if len(data) != 4:
			return Student.invalid()
		
		try: ret = Student(data[0], data[1], int(data[2]), data[3])
		except: return Student.invalid()
		
		return ret
	
	@staticmethod
	def invalid():
		return Student('Invalid', 'Invalid', 0, '00-00-0000')
