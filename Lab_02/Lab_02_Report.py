# Question_01
class Student1:
    pass
class Marks:
    pass

sk_nahid = Student1()
passed = Marks()
check_student = isinstance(sk_nahid, Student1)
print("sk_nahid is a instance of class Student--", check_student)
check_marks = isinstance(sk_nahid, Marks)
print("sk_nahid is a instance of class Marks--", check_marks)
check_student = isinstance(passed, Student1)
print("passed is a instance of class Student--", check_student)
check_marks = isinstance(passed, Marks)
print("passed is a instance of class Marks--", check_marks)
check_student_subclass = isinstance(Student1, object)
print("Student class is a subclass of object--", check_student_subclass)
check_marks_subclass = isinstance(Marks, object)
print("Marks class is a subclass of object--", check_marks_subclass)

# Question_02
class Student2:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

e1 = Student2("Sk. Nahid", 22)
print(e1.name, e1.marks)
e1.name = "Ahmed"
e1.marks = 23
print("modified value:", e1.name, e1.marks)

# Question_03
class Student3:
    def __init__(self, ID, Name):
        self.ID = ID
        self.Name = Name
    
e1 = Student3("201902073", "Sk. Nahid")
print(e1.ID, e1.Name)
# adding new attribute to this class
e1.Marks = 82
print("New attribute=> Marks: ",e1.Marks)
# deleting attribute
del e1.Marks
print("Deleted attribute=> Marks: ",e1.Marks)

# Question_04
class Student4:
    def __init__(self, StudentID, StudentName):
        self.StudentID = StudentID
        self.StudentName = StudentName
    def function(self):
        print(f'Student name is {self.StudentName} & ID is {self.StudentID}')

e1 = Student4("201902073", "Sk. Nahid")
e1.function()