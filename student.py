from dataclasses import dataclass

@dataclass
class Student:
	name : str
	age : int
	birthday : str

	def __str__(self):
		return f'{self.name} {self.age} {self.birthday}'

	@staticmethod
	def parse(str):
		data = str.split(' ')
		if len(data) != 3:
			return Student('Old/invalid format', -1, 'None')
		return Student(data[0], int(data[1]), data[2])
