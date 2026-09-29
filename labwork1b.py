# ==========================================
# PRACTICAL WORK 1: STUDENT MARK MANAGEMENT
# ==========================================


# ---------- INPUT STUDENTS ----------
def input_students():
    students = []

    n = int(input("Enter number of students: "))

    for i in range(n):
        print("\nStudent", i + 1)

        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter date of birth: ")

        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }

        students.append(student)

    return students


# ---------- INPUT COURSES ----------
def input_courses():
    courses = []

    n = int(input("\nEnter number of courses: "))

    for i in range(n):
        print("\nCourse", i + 1)

        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")

        course = {
            "id": course_id,
            "name": course_name
        }

        courses.append(course)

    return courses


# ---------- LIST STUDENTS ----------
def list_students(students):
    print("\n===== STUDENT LIST =====")

    for student in students:
        print(
            student["id"],
            "-",
            student["name"],
            "-",
            student["dob"]
        )


# ---------- LIST COURSES ----------
def list_courses(courses):
    print("\n===== COURSE LIST =====")

    for course in courses:
        print(
            course["id"],
            "-",
            course["name"]
        )


# ---------- INPUT MARKS ----------
def input_marks(students, courses):
    marks = {}

    list_courses(courses)

    course_id = input("\nEnter course ID to input marks: ")

    course_found = False

    for course in courses:
        if course["id"] == course_id:
            course_found = True

    if course_found == False:
        print("Course not found!")
        return marks

    marks[course_id] = {}

    print("\nEnter marks for course:", course_id)

    for student in students:
        mark = float(
            input("Enter mark for " + student["name"] + ": ")
        )

        marks[course_id][student["id"]] = mark

    return marks


# ---------- SHOW MARKS ----------
def show_marks(students, courses, marks):
    list_courses(courses)

    course_id = input("\nEnter course ID to show marks: ")

    if course_id not in marks:
        print("No marks found for this course.")
        return

    print("\n===== STUDENT MARKS =====")

    for course in courses:
        if course["id"] == course_id:
            print("Course:", course["name"])

    for student in students:
        student_id = student["id"]

        if student_id in marks[course_id]:
            print(
                student["id"],
                "-",
                student["name"],
                "- Mark:",
                marks[course_id][student_id]
            )


# ==========================================
# MAIN PROGRAM
# ==========================================

students = input_students()

courses = input_courses()

list_students(students)

list_courses(courses)

marks = input_marks(students, courses)

show_marks(students, courses, marks)