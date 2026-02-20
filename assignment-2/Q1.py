# 1. Base Class (Parent)
class User:
    def __init__(self , name , user_id):
        # Encapsulation to make variable private
        self.__name = name
        self.__user_id = user_id

    def get_name(self):
        return self.__name
    
    #Polymorphism:Method will be changed in child classes
    def display_details(self):
        print(f"ID: {self.__user_id} | Name: {self.__name}")

# 2. Student Class (inherits from user)
class Student(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.course = "Not Enrolled"

    def enroll(self, course_name): #allow students to enroll
        self.course = course_name

    def display_details(self):
        super().display_details()
        print(f"Role: Student | Course: {self.course}")

# 3. Mentor Class (Inherits from User)
class Mentor(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.students_list = []

    def assign_student(self, student_name): #Metor see assigned students
        self.students_list.append(student_name)

    def display_details(self):
        super().display_details()
        print(
            f"Role: Mentor | Assigned Students: "
            f"{', '.join(self.students_list) if self.students_list else 'None'}"
        )  
# 4. Admin Class
class Admin(User):
    def display_details(self , students , Mentors): # admin views all details
        print("\n-- All Registered Students --")
        for s in students: s.display_details()
        print("\n-- All Registered Mentors --")
        for m in Mentors: m.display_details()


students = []
mentors = []
admin = Admin("Boss", "A01")

while True:
    print("\n--- EdTech Management System ---")
    print("1. Add Student\n2. Add Mentor\n3. Enroll student\n4. Admin view\n5. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        name = input("Enter Student Name: ")
        sid = input("Enter Student ID: ")
        students.append(Student(name, sid))

    elif choice == '2':
        name = input("Enter Mentor Name: ")
        mid = input("Enter Mentor ID: ")
        mentors.append(Mentor(name, mid))

    elif choice == '3':
        if not students:
            print("No students available to enroll.")
            continue

        s_name = input("Enter Student Name to enroll: ")
        c_name = input("Enter Course Name: ")
    
        found = False
        for s in students:
            if s.get_name().strip().lower() == s_name.strip().lower():
                s.enroll(c_name)
                print("Student enrolled successfully.")
                found = True
                break

        if not found:
            print("Studen not found.")

    elif choice == '4':
        admin.display_details(students, mentors)

    elif choice == '5':
        break

    else:
        print("Invalid Option.")
