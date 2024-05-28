from student import Student

class Service:
	def __init__(self, encryption_key : int):
		self.key = encryption_key

	@staticmethod
	def __encrypt(text : str, key : int):
		new_text = [None] * len(text)
		for i, c in enumerate(text):
			if 'A' <= c and c <= 'Z':
				new_text[i] = chr((ord(c) + key - ord('A')) % (ord('Z') - ord('A') + 1) + ord('A'))
			elif 'a' <= c and c <= 'z':
				new_text[i] = chr((ord(c) + key - ord('a')) % (ord('z') - ord('a') + 1) + ord('a'))
			else:
				new_text[i] = c
		return ''.join(new_text)

	def encrypt(self, text : str):
		return Service.__encrypt(text, self.key)

	def decrypt(self, text : str):
		return Service.__encrypt(text, -self.key)

	def add_student(self, student):
		with open('db.txt', 'a') as f:
			f.write(self.encrypt(f'{student}\n'))

	def get_students(self) -> list[Student]:
		ret = []
		with open('db.txt', 'r') as f:
			for line in f:
				try:
					student = Student.parse(self.decrypt(line.strip()))
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
