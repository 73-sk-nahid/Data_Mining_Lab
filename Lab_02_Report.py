# Question_01
class Student:
    pass
class Marks:
    pass

sk_nahid = Student()
passed = Marks()
check_student = isinstance(sk_nahid, Student)
print("sk_nahid is a instance of class Student--", check_student)
check_marks = isinstance(sk_nahid, Marks)
print("sk_nahid is a instance of class Marks--", check_marks)
check_student = isinstance(passed, Student)
print("passed is a instance of class Student--", check_student)
check_marks = isinstance(passed, Marks)
print("passed is a instance of class Marks--", check_marks)
check_student_subclass = isinstance(Student, object)
print("Student class is a subclass of object--", check_student_subclass)
check_marks_subclass = isinstance(Marks, object)
print("Marks class is a subclass of object--", check_marks_subclass)
