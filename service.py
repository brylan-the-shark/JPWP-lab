from student import Student

class Service:
	def add_student(self, student):
		with open('db.txt', 'a') as f:
			f.write(f'{student}\n')

	def get_students(self) -> list[Student]:
		ret = []
		with open('db.txt', 'r') as f:
			for line in f:
				try:
					student = Student.parse(line.strip())
				except ValueError:
					student = Student.invalid()
				
				ret.append(student)
		return ret
	
	def remove_student(self, idx):
		with open('db.txt', 'r') as f:
			lines = f.readlines()
		
		with open('db.txt', 'w') as f:
			for i, line in enumerate(lines):
				if i != idx:
					f.write(line)

	def find_students(self, **by):
		ret = []
		for s in self.get_students():
			if vars(s).items() >= by.items():
				ret.append(s)
		return ret
