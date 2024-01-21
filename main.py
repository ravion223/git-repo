import sqlite3

db = sqlite3.connect("university.db")

db.execute(
    '''CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50),
        age INTEGER,
        major VARCHAR(50));'''
)

db.execute(
    '''CREATE TABLE IF NOT EXISTS courses(
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name VARCHAR(50),
        instructor VARCHAR(50));'''
)

db.execute(
    '''CREATE TABLE IF NOT EXISTS student_course(
        course_id INTEGER FORGEIN KEY,
        student_id INTEGER FORGEIN KEY,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students (id),
        FOREIGN KEY (course_id) REFERENCES courses (course_id));'''
)

def add_student(db, name, age, major):
    db.execute(f'''INSERT INTO students (name, age, major)
               VALUES (?,?,?)''', (name, age, major))
    db.commit()
    
def add_course(db, course_name, instructor):
    db.execute(f'''INSERT INTO courses (course_name, instructor)
               VALUES (?,?)''', (course_name, instructor))
    db.commit()

def add_student_to_course(db, student_id, course_id):
    db.execute(f'''INSERT INTO student_course(student_id, course_id)
               VALUES  (?, ?)''', (student_id, course_id))
    db.commit()
    
def get_students(db):
    students = db.execute('''SELECT * FROM students''')
    return students

def get_courses(db):
    courses = db.execute('''SELECT * FROM courses''')
    return courses

def get_student_course(db, course_id):
    student_course = db.execute(f'''SELECT * FROM students
                                JOIN student_course ON students.id = student_course.student_id
                                WHERE student_course.course_id = ?''', (course_id,))
    return student_course


while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    match choice:
        case "1":
            name = input("Input student's name")
            age = int(input("Input student's age"))
            major = input("Input student's major")
            add_student(db, name, age, major)
            print(f"Student {name} added successfully")
        case "2":
            course_name = input("Input course name")
            instructor = input("Input instructor's name")
            add_course(db, course_name, instructor)
            print(f"Course {course_name} added successfully")
        case "3":
            students = get_students(db)
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Major: {student[3]}")
        case "4":
            courses = get_courses(db)
            for course in courses: 
                print(f"ID: {course[0]}, Course name: {course[1]}, Course instructor: {course[2]}")
        case "5":
            student_id = int(input("Input student's id"))
            course_id = int(input("Input course id"))
            add_student_to_course(db, student_id, course_id)
            print("Student added to course successfully")
        case "6":
            course_id = int(input("Input course id"))
            students_courses = get_student_course(db, course_id)
            for student_course in students_courses:
                print(f"ID: {student_course[0]}, Name: {student_course[1]}, Age: {student_course[2]}, Major: {student_course[3]}")
        case "7":
            print("Have a good day!")
            break
        case _:
            print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")