# Exercise 5.4.3
# Define a Python function student(). Using function attributes display the names of all arguments.
def student(id, name):
    print(f'\nStudents ID is {id} & name is {name}')

student(201902073, "Sk. Nahid")

# Write a Python function studentId () which will print the id of a student (studentId). 
# If the user passes an argument studentId or studentId the function will print the student name and class
def students(id):
    students_info = {
        "201902073" : {"Name" : "Sk. Nahid", "Section" : "D2"},
        "201902067" : {"Name" : "Shamim Ahmed", "Section" : "D2"},
    }

    if id in students_info:
        info = students_info[id]
        print(f"\nStudent ID: {id}")
        print(f"Student Name: {info['Name']}")
        print(f"Student Section: {info['Section']}")
    else:
        print(f'\nNo info for this: {id} ')

students('201902073')
students('201902064')
students('201902067')