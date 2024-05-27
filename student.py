from dataclasses import dataclass

@dataclass
class Student:
	name : str
	age : int
	birthday : str

	def __str__(self):
		return f'{self.name}\t{self.age}\t{self.birthday}'

	@staticmethod
	def parse(str):
		data = str.split('\t')
		if len(data) != 3:
			return Student('Old/invalid format', -1, 'None')
		return Student(data[0], int(data[1]), data[2])
