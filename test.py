class Student(object):
	bb = "testssss"
	def __init__(self):
		self.aa = "test"

if __name__ == "__main__":
	st = Student()
	print st.aa
	print st.bb
	
	print Student.bb
	setattr(Student,"cc","abcccccc")
	print Student.cc
	print st.cc
