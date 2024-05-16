class Student:
	def __init__(self, name, age, birthday):
		self.name = name
		self.age = age
		self.birthday = birthday

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def __str__(self):
		return f'{self.name} {self.age} {self.birthday}'

	@staticmethod
	def parse(str):
		data = str.split(' ')
		if len(data) != 3:
			return Student('Old/invalid format', -1, 'None')
		return Student(data[0], int(data[1]), data[2])
