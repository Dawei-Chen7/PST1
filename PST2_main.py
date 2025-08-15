# MSMS.py - The In-Memory Prototype.
import json
import datetime

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

# TODO: Assign all three parameters(course code, name)

# --- In-Memory Databases ---
# TODO: Create the global data stores.
student_db = []
teacher_db = []
course_db = []
next_student_id = 1
next_teacher_id = 1
next_course_code = 1
app_data = {} # This global dictionary will hold ALL our data.
DATA_FILE = "msms.json"

# --- Core Persistence Engine ---
def load_data(path=DATA_FILE):
    """Loads all application data from a JSON file."""
    global app_data
    try:
        with open(path, 'r') as f:
            # TODO: Use json.load(f) to load the file's content into the global 'app_data' variable.
            app_data = json.load(f)
            print("Data loaded successfully.")
    except FileNotFoundError:
        print("Data file not found. Initializing with default structure.")
        # TODO: If the file doesn't exist, initialize 'app_data' with a default dictionary.
        # It should have keys like: "students", "teachers", "attendance", "next_student_id", "next_teacher_id".
        # The lists should be empty and the IDs should start at 1.
        app_data = {
            "students": [],
            "teachers": [],
            "courses": [],
            "attendance": [],
            "next_student_id": 1,
            "next_teacher_id": 1,
            "next_course_code": 1
        }

def save_data(path=DATA_FILE):
    """Saves all application data to a JSON file."""
    # TODO: Open the file at 'path' in write mode ('w').
    # Use json.dump() to write the global 'app_data' dictionary to the file.
    # Use the 'indent=4' argument in json.dump() to make the file readable.
    with open(path, 'w') as f:
        json.dump(app_data, f, indent=4)
    print("Data saved successfully.")

def add_student(name):
    """Adds a teacher dictionary to the data store."""
    # TODO: Get the next student ID from app_data['next_student_id'].
    student_id = app_data['next_student_id']
    # TODO: Create a new teacher dictionary with 'id', 'name', and 'speciality' keys.
    new_student = {"id": student_id, "name": name}
    # TODO: Append the new dictionary to the app_data['students'] list.
    app_data['students'].append(new_student)
    # TODO: Increment the 'next_student_id' in app_data.
    app_data['next_student_id'] += 1
    print(f"Core: Student '{name}' added.")

def add_teacher(name, speciality):
    """Adds a teacher dictionary to the data store."""
    # TODO: Get the next teacher ID from app_data['next_teacher_id'].
    teacher_id = app_data['next_teacher_id']
    # TODO: Create a new teacher dictionary with 'id', 'name', and 'speciality' keys.
    new_teacher = {"id": teacher_id, "name": name, "speciality": speciality}
    # TODO: Append the new dictionary to the app_data['teachers'] list.
    app_data['teachers'].append(new_teacher)
    # TODO: Increment the 'next_teacher_id' in app_data.
    app_data['next_teacher_id'] += 1
    print(f"Core: Teacher '{name}' added.")

def create_course(course_name):
    """Creates a course object and adds it to the database."""
    # TODO: Create a new Course object using the next available code.
    course_code = app_data['next_course_id']
    new_course = {"code": course_code, "name": course_name}
    # TODO: Append the new_course to the course_db list.
    app_data["courses"].append(new_course)
    # TODO: Increment the next_course_code counter.
    app_data["next_course_code"] += 1
    print(f"Core: Course '{course_name}' added successfully.")

def update_teacher(teacher_id, **fields):
    """Finds a teacher by ID and updates their data with provided fields."""
    # TODO: Loop through the app_data['teachers'] list.
    for teacher in app_data['teachers']:
        # TODO: If a teacher's 'id' matches teacher_id:
        if teacher['id'] == teacher_id:
            # Use the .update() method on the teacher dictionary to apply the 'fields'.
            teacher.update(fields)
            print(f"Teacher {teacher_id} updated.")
            return
    print(f"Error: Teacher with ID {teacher_id} not found.")

def update_student(student_id, **fields):
    """Finds a teacher by ID and updates their data with provided fields."""
    # TODO: Loop through the app_data['students'] list.
    for student in app_data['students']:
        # TODO: If a student's 'id' matches student_id:
        if student['id'] == student_id:
            # Use the .update() method on the student dictionary to apply the 'fields'.
            student.update(fields)
            print(f"Student {student_id} updated.")
            return
    print(f"Error: Teacher with ID {student_id} not found.")

def remove_student(student_id):
    """Removes a student from the data store."""
    # TODO: Find the student dictionary in app_data['students'] with the matching ID.
    for student in app_data['students']:
        if student['id'] == student_id:
            app_data['students'].remove(student)
            save_data(DATA_FILE)
            print(f"Student {student_id} is removed")
            return
        print(f"Error: Student with ID {student_id} is not found.")

def remove_teacher(teacher_id):
    """Removes a teacher from the data store."""
    # TODO: Find the teacher dictionary in app_data['teachers'] with the matching ID.
    for teacher in app_data['teachers']:
        if teacher['id'] == teacher_id:
            # If found, use the .remove() method on the list to delete it.
            # A list comprehension is a clean way to do this:
            # app_data['students'] = [s for s in app_data['students'] if s['id'] != student_id]
            app_data['teachers'].remove(teacher)
            save_data(DATA_FILE)
            print(f"Teacher {teacher_id} is removed")
            return
        print(f"Error: Teacher with ID {teacher_id} is not found.")

def list_students():
    """Prints all students in the database."""
    print("\n--- Student List ---")
    # TODO: Loop through student_db. For each student, print their ID, name, and their enrolled_in list.
    for student in app_data['students']:
        print(f"  ID: {student['id']}, Name: {student['name']}, Enrolled in: {student['enroll_in']}")
    if app_data['students'] is None:
        print("No students in the system.")
        return

def list_teachers():
    """Prints all teachers in the database."""
    # TODO: Implement the logic to list all teachers, similar to list_students().
    print("\n--- Teacher List ---")
    for teacher in app_data['teachers']:
        print(f"  ID: {teacher['id']}, Name: {teacher['name']}, Speciality: {teacher['speciality']}")
    if app_data['teachers'] is None:
        print("No teachers in the system.")
        return

def list_course():
    """Prints all teachers in the database."""
    # TODO: Implement the logic to list all courses, similar to list_students().
    print("\n--- Course List ---")
    for course in app_data['courses']:
        print(f"  Code: {course['code']}, Subject: {course['name']}")
     if app_data['courses'] is None:
        print("No courses in the system.")
        return

def find_students(name):
    """Finds students by name."""
    print(f"\n--- Finding Students matching '{name}' ---")
    # TODO: Create an empty list to store results.
    student_list = []
    # Loop through student_db. If the search 'term' (case-insensitive) is in the student's name,
    # add them to your results list.
    for student in app_data['students']:
        if student['name'].upper == name.upper():
            student_list.append(student)
    # After the loop, if the results list is empty, print "No match found."
    if not student_list:
        print("No match found.")
    # Otherwise, print the details for each student in the results list.
    else:
        for student in student_list:
            print(f" ID: {student['id']}, Name: {student['name']}")

def find_teachers(info):
    """Finds teachers by name or speciality."""
    # TODO: Implement this function similar to find_students, but check
    teacher_list = []
    # Loop through teacher_db. If the search 'term' (case-insensitive) is in the teacher's name,
    # add them to your results list.
    for teacher in app_data['teachers']:
        if teacher['name'].upper() == info.upper() or teacher['speciality'].upper() == info.upper():
            teacher_list.append(teacher)
    # After the loop, if the results list is empty, print "No match found."
    if not teacher_list:
        print("No match found.")
    else:
        for teacher in teacher_list:
            print(f" ID: {teacher['id']}, Name: {teacher['name']}, speciality: {teacher['speciality']}")
    # for the term in BOTH the teacher's name AND their speciality.

def find_student_by_id(student_id):
    """A new helper to find one student by their exact ID."""
    # TODO: Loop through student_db. If a student's ID matches student_id, return the student object.
    result = None
    for student in app_data['students']:
        if student['id'] == student_id:
            result = student
            #print(f"find student: {student.name}, course:{student.enroll_in}")
    # TODO: If the loop finishes without finding a match, return None.
    return result

def front_desk_register(name, instrument):
    """High-level function to register a new student and enrol them."""
    # TODO: Create a new Student object, add it to student_db, and increment the ID.
    student_id = app_data['next_student_id']
    # TODO: Create a new teacher dictionary with 'id', 'name', and 'speciality' keys.
    new_student = {"id": student_id, "name": name, "instrument": instrument}
    # TODO: Append the new dictionary to the app_data['students'] list.
    app_data['students'].append(new_student)
    app_data['next_student_id'] += 1
    # TODO: Immediately call front_desk_enrol() using the new student's ID and the provided instrument.
    front_desk_enrol(new_student['id'], instrument)
    print(f"Front Desk: Successfully registered '{name}' and enrolled them in '{instrument}'.")

def front_desk_enrol(student_id, instrument):
    """High-level function to enrol an existing student in a course."""
    # TODO: Use your new find_student_by_id() helper.
    student = find_student_by_id(student_id)
    # TODO: If the student is found, append the instrument to their 'enrolled_in' list.
    if student:
        student["instruments"] = [instrument]
        print(f"Front Desk: Enrolled student '{student_id}' in '{instrument}'.")
    else:
        # TODO: If the student is not found, print an error message like "Error: Student ID not found."
        print(f"Error: Student ID '{student_id}' not found.")

def front_desk_enrol_updating(student_id, course_existing, course_new):
    # TODO: Update the subject of existing students.
    student = find_student_by_id(student_id)
    if student:
        if course_existing.upper() in student.enroll_in:
            student.enroll_in.remove(course_existing.upper())
            student.enroll_in.append(course_new.upper())
            print(f"Front Desk: update student '{student_id}' in '{course_new}'")
        else:
            print(f"Front Desk: student '{student_id}' have no '{course_existing}' class")
    else:
        # TODO: If the student is not found, print an error message like "Error: Student ID not found."
        print(f"Error: Student ID '{student_id}' not found.")

def find_teacher_by_id(teacher_id):
    """A new helper to find one teacher by their exact ID."""
    # TODO: Loop through student_db. If a student's ID matches student_id, return the student object.
    for teacher in teacher_db:
        if teacher.id == teacher_id:
            print(f"Find teacher: {teacher.name}, speciality: {teacher.speciality}")
    # TODO: If the loop finishes without finding a match, return None.
    return None

def front_desk_lookup(term):
    """High-level function to search everything."""
    print(f"\n--- Performing lookup for '{term}' ---")
    find_students(term)
    find_teachers(term)


def check_in(student_id, course_id, timestamp=None):
    """Records a student's attendance for a course."""
    if timestamp is None:
        # TODO: Get the current time as a string using datetime.datetime.now().isoformat()
        timestamp = datetime.datetime.now().isoformat()

    # TODO: Create a check-in record dictionary.
    # It should contain 'student_id', 'course_id', and 'timestamp'.
    check_in_record = {
        "student_id": student_id,
        "course_id": course_id,
        "timestamp": timestamp
    }
    # TODO: Append this new record to the app_data['attendance'] list.
    app_data['attendance'].append(check_in_record)
    print(f"Receptionist: Student {student_id} checked into {course_id}.")


def print_student_card(student_id):
    """Creates a text file badge for a student."""
    # TODO: Find the student dictionary in app_data['students'].
    student_to_print = None
    for s in app_data['students']:
        if s['id'] == student_id:
            student_to_print = s
            break
    if student_to_print:
        # TODO: Create a filename, e.g., f"{student_id}_card.txt".
        filename = f"{student_id}_card.txt"
        # TODO: Open the file in write mode ('w').
        with open(filename, 'w') as f:
            # Write the student's details to the file in a nice format.
            f.write("========================\n")
            f.write(f"  MUSIC SCHOOL ID BADGE\n")
            f.write("========================\n")
            f.write(f"ID: {student_to_print['id']}\n")
            f.write(f"Name: {student_to_print['name']}\n")
            f.write(f"Enrolled In: {', '.join(student_to_print.get('enrolled_in', []))}\n")
        print(f"Printed student card to {filename}.")
    else:
        print(f"Error: Could not print card, student {student_id} not found.")

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
        print("3. Change course for existing students")
        print("4. Lookup Student or Teacher")
        print("5. Find teacher by ID")
        print("6. Find student by ID")
        print("7. (Admin) List all Students")
        print("8. (Admin) List all Teachers")
        print("9. (Admin) list all Courses")
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
            # TODO: Prompt for student ID (as an int) and instrument, then call front_desk_enrol_updating.
            student_id = int(input("Enter student ID: "))
            course_existing = input("Enter the course you want to change: ")
            course_new = input("Enter the new course you want to choose: ")
            front_desk_enrol_updating(student_id, course_existing,course_new)
        elif choice == '4':
            # TODO: Prompt for a search term, then call front_desk_lookup.
            term = input("Enter search term(1, name or specialty. 2, ID): ")
            front_desk_lookup(term)
        elif choice == '5':
            teacher_id = int(input("Enter teacher ID: "))
            find_teacher_by_id(teacher_id)
        elif choice == '6':
            student_id = int(input("Enter student ID: "))
            find_student_by_id(student_id)
        elif choice == '7':
            list_students()
        elif choice == '8':
            list_teachers()
        elif choice == '9':
            list_course()
        elif choice.lower() == 'q':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# --- Program Start ---
if __name__ == "__main__":
    main()