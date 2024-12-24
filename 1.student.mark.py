class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            self.students.append(Student(student_id, name, dob))

            
    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.courses.append(Course(course_id, name))

    def input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        for student in self.students:
            mark = float(input(f"Enter marks for {student.name} (ID: {student.student_id}): "))
            student.marks[course_id] = mark

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}")

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}")

    def show_student_marks(self):
        course_id = input("Enter course ID to show marks: ")
        print(f"Marks for course ID {course_id}:")
        for student in self.students:
            if course_id in student.marks:
                print(f"{student.name}: {student.marks[course_id]}")
            else:
                print(f"{student.name}: No marks entered.")

# Example of using the StudentMarkManagement class
if __name__ == "__main__":
    manager = StudentMarkManagement()
    manager.input_students()
    manager.input_courses()
    manager.input_marks()
    manager.list_courses()
    manager.list_students()
    manager.show_student_marks()
