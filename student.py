import re

class Student:
	name: str
	surname: str
	age: int
	birthday: str
	index: str

	def __init__(self, name, surname, age, birthday, index):
		if not re.fullmatch('[A-Z][a-z]*', name):
			raise ValueError('Name must only contain letters and be capitalized')
		if not re.fullmatch('[A-Z][a-z]*', surname):
			raise ValueError('Surame must only contain letters and be capitalized')
		if age < 0 or age > 150:
			raise ValueError('Age must be in range 0 to 150')
		if not re.fullmatch('\d{2}-\d{2}-\d{4}', birthday):
			raise ValueError('Birthday must be in DD-MM-YYYY format')
		if not re.fullmatch('\d{6}', index):
			raise ValueError('Index must contain 6 digits only')

		self.name = name
		self.surname = surname
		self.age = age
		self.birthday = birthday
		self.index = index

	def __str__(self):
		return '\t'.join(str(v) for v in vars(self).values())

	@staticmethod
	def parse(str):
		data = str.split('\t')

		if len(data) != 5:
			raise ValueError('Invalid row')
		
		return Student(data[0], data[1], int(data[2]), data[3], data[4])
	
	@staticmethod
	def invalid():
		return Student('Invalid', 'Invalid', 0, '00-00-0000', '000000')
