def input_number_of_students():
    return int(input("Nhập số lượng sinh viên trong lớp: "))

def input_student_info(num_students):
    students = []
    for _ in range(num_students):
        student_id = input("Nhập ID sinh viên: ")
        name = input("Nhập tên sinh viên: ")
        dob = input("Nhập ngày sinh (DD/MM/YYYY): ")
        students.append((student_id, name, dob))
    return students

def input_number_of_courses():
    return int(input("Nhập số lượng khóa học: "))

def input_course_info(num_courses):
    courses = []
    for _ in range(num_courses):
        course_id = input("Nhập ID khóa học: ")
        course_name = input("Nhập tên khóa học: ")
        courses.append((course_id, course_name))
    return courses

def input_student_marks(courses, students):
    marks = {}
    for course in courses:
        course_id = course[0]
        marks[course_id] = {}
        for student in students:
            student_id = student[0]
            mark = float(input(f"Nhập điểm cho sinh viên {student[1]} ({student_id}) trong khóa học {course[1]}: "))
            marks[course_id][student_id] = mark
    return marks

def list_courses(courses):
    print("\nDanh sách khóa học:")
    for course in courses:
        print(f"ID: {course[0]}, Tên: {course[1]}")

def list_students(students):
    print("\nDanh sách sinh viên:")
    for student in students:
        print(f"ID: {student[0]}, Tên: {student[1]}, Ngày sinh: {student[2]}")

def show_student_marks(marks, courses):
    course_id = input("Nhập ID khóa học để xem điểm: ")
    if course_id in marks:
        print(f"\nĐiểm của sinh viên trong khóa học {course_id}:")
        for student_id, mark in marks[course_id].items():
            print(f"Sinh viên ID: {student_id}, Điểm: {mark}")
    else:
        print("Khóa học không tồn tại.")

def main():
    num_students = input_number_of_students()
    students = input_student_info(num_students)

    num_courses = input_number_of_courses()
    courses = input_course_info(num_courses)

    marks = input_student_marks(courses, students)

    list_courses(courses)
    list_students(students)
    show_student_marks(marks, courses)

if __name__ == "__main__":
    main()
