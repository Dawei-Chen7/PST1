# MSMS.py - The In-Memory Prototype.

# --- Data Models ---
class Student:
    """A blueprint for student objects. Holds their info."""
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        # TODO: Initialize an empty list called 'enrolled_in' to store instrument names.
        self.enroll_in = []

class Teacher:
    """A blueprint for teacher objects."""
    def __init__(self, teacher_id, name, speciality):
        # TODO: Assign all three parameters (teacher_id, name, speciality)
        # to instance variables (e.g., self.id = teacher_id).
        self.id = teacher_id
        self.name = name
        self.speciality = speciality
        self.teaching = []

class Course:
    def __init__(self, course_code, course_name):
        self.code = course_code
        self.name = course_name
        self.teacher = []
        self.student = []

# TODO: Assign all three parameters(course code, name)

# --- In-Memory Databases ---
# TODO: Create the global data stores.
student_db = []
teacher_db = []
course_db = []
next_student_id = 1
next_teacher_id = 1
next_course_code = 1

# --- Core Helper Functions ---

def add_student(name):
    """Creats a Student object and adds it to database."""
    global next_student_id
    # TODO: Create a new student object using the next available ID.
    new_student = Student(next_student_id, name)
    # TODO: Append the new_student to the student_db list.
    student_db.append(new_student)
    # TODO: Increment the next_student_id counter.
    next_student_id += 1
    print(f"Core: Student '{name}' added successfully.")

def add_teacher(name, speciality):
    """Creates a Teacher object and adds it to the database."""
    global next_teacher_id
    # TODO: Create a new Teacher object using the next available ID.
    new_teacher = Teacher(next_teacher_id, name, speciality)
    # TODO: Append the new_teacher to the teacher_db list.
    teacher_db.append(new_teacher)
    # TODO: Increment the next_teacher_id counter.
    next_teacher_id += 1
    print(f"Core: Teacher '{name}' added successfully.")

def create_course(course_code, course_name):
    """Creates a course object and adds it to the database."""
    global next_course_code
    new_course = Course(course_code,course_name)
    course_db.append(new_course)
    next_course_code += 1
    print(f"Core: Course '{course_name}' added successfully.")

def list_students():
    """Prints all students in the database."""
    print("\n--- Student List ---")
    if not student_db:
        print("No students in the system.")
        return
    # TODO: Loop through student_db. For each student, print their ID, name, and their enrolled_in list.
    for student in student_db:
        print(f"  ID: {student.id}, Name: {student.name}, Enrolled in: {student.enrolled_in}")

def list_teachers():
    """Prints all teachers in the database."""
    # TODO: Implement the logic to list all teachers, similar to list_students().
    print("\n--- Teacher List ---")
    for teacher in teacher_db:
        print(f"  ID: {teacher.id}, Name: {teacher.name}, Speciality: {teacher.speciality}")

def list_course():
    print("\n--- Teacher List ---")
    for course in course_db:
        print(f"  Code: {course.code}, Subject: {course.name}, Lecturer: {course.teacher}")

def find_students(info):
    """Finds students by name."""
    print(f"\n--- Finding Students matching '{info}' ---")
    # TODO: Create an empty list to store results.
    student_list = []
    # Loop through student_db. If the search 'term' (case-insensitive) is in the student's name,
    # add them to your results list.
    for student in student_db:
        if student.name == info:
            student_list.append(student)
    # After the loop, if the results list is empty, print "No match found."
    if not student_list:
        print("No match found.")
    # Otherwise, print the details for each student in the results list.
    else:
        for student in student_list:
            print(f" ID: {student.id}, Name: {student.name}")

def find_teachers(info):
    """Finds teachers by name or speciality."""
    # TODO: Implement this function similar to find_students, but check
    teacher_list = []
    for teacher in teacher_db:
        if teacher.name.upper() == info.upper() or teacher.speciality.upper() == info.upper():
            teacher_list.append(teacher)
    if not teacher_list:
        print("No match found.")
    else:
        for teacher in teacher_list:
            print(f" ID: {teacher.id}, Name: {teacher.name}")
    if not teacher_list:
        print("No match found.")
    else:
        for teacher in teacher_list:
            print(f" ID: {teacher.id}, Name: {teacher.name}, speciality: {teacher.speciality}")
    # for the term in BOTH the teacher's name AND their speciality.


