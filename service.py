from student import Student

class Service:
	def add_student(self, student):
		with open('db.txt', 'a') as file:
			file.write(f'{student}\n')

	def get_students(self) -> list[Student]:
		ret = []
		with open('db.txt', 'r') as file:
			for line in file:
				ret.append(Student.parse(line.strip()))
		return ret

	def find_students(self, **by):
		ret = []
		for s in self.get_students():
			if vars(s).items() >= by.items():
				ret.append(s)
		return ret
