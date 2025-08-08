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
    def __init__(self, teacher_id, name):
        # TODO: Assign all three parameters (teacher_id, name, speciality)
        # to instance variables (e.g., self.id = teacher_id).
        self.id = teacher_id
        self.name = name
        self.speciality = None
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
    new_teacher = Teacher(next_teacher_id, name)
    # TODO: Set speciality to teacher
    new_teacher.speciality = speciality
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

def find_student_by_id(student_id):
    """A new helper to find one student by their exact ID."""
    # TODO: Loop through student_db. If a student's ID matches student_id, return the student object.
    for student in student_db:
        if student.id == student_id:
            return student
    # TODO: If the loop finishes without finding a match, return None.
    return None

def front_desk_register(name, instrument):
    """High-level function to register a new student and enrol them."""
    global next_student_id
    # TODO: Create a new Student object, add it to student_db, and increment the ID.
    new_student = Student(next_student_id, name)
    student_db.append(new_student)
    next_student_id += 1
    # TODO: Immediately call front_desk_enrol() using the new student's ID and the provided instrument.
    front_desk_enrol(new_student.id, instrument)
    print(f"Front Desk: Successfully registered '{name}' and enrolled them in '{instrument}'.")

def front_desk_enrol(student_id, instrument):
    """High-level function to enrol an existing student in a course."""
    # TODO: Use your new find_student_by_id() helper.
    student = find_student_by_id(student_id)
    # TODO: If the student is found, append the instrument to their 'enrolled_in' list.
    if student:
        student.enroll_in.append(instrument)
        print(f"Front Desk: Enrolled student '{student_id}' in '{instrument}'.")
    else:
        # TODO: If the student is not found, print an error message like "Error: Student ID not found."
        print(f"Error: Student ID '{student_id}' not found.")

def front_desk_lookup(term):
    """High-level function to search everything."""
    print(f"\n--- Performing lookup for '{term}' ---")
    find_students(term)
    find_teachers(term)


# --- Main Application ---
def main():
    """Runs the main interactive menu for the receptionist."""
    # Pre-populate some data for easy testing
    add_teacher("Dr. Keys", "Piano")
    add_teacher("Ms. Fret", "Guitar")

    while True:
        print("\n===== Music School Front Desk =====")
        print("1. Register New Student")
        print("2. Enrol Existing Student")
        print("3. Lookup Student or Teacher")
        print("4. (Admin) List all Students")
        print("5. (Admin) List all Teachers")
        print("q. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # TODO: Prompt for student name and instrument, then call front_desk_register.
            name = input("Enter student name: ")
            instrument = input("Enter instrument to enrol in: ")
            front_desk_register(name, instrument)
        elif choice == '2':
            # TODO: Prompt for student ID (as an int) and instrument, then call front_desk_enrol.
            try:
                student_id = int(input("Enter student ID: "))
                instrument = input("Enter instrument to enrol in: ")
                front_desk_enrol(student_id, instrument)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '3':
            # TODO: Prompt for a search term, then call front_desk_lookup.
            term = input("Enter search term: ")
            front_desk_lookup(term)
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_teachers()
        elif choice.lower() == 'q':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# --- Program Start ---
if __name__ == "__main__":
    main()
