class Student:
    def __init__(self, student_id, name, age, grade, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.email = email
    
    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Grade: {self.grade} | Email: {self.email}"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}
    
    def add_student(self, student_id, name, age, grade, email):
        if student_id in self.students:
            print(f"Error: Student with ID {student_id} already exists!")
            return False
        
        student = Student(student_id, name, age, grade, email)
        self.students[student_id] = student
        print(f"Student {name} added successfully!")
        return True
    
    def view_all_students(self):
        if not self.students:
            print("No students in the system.")
            return
        
        print("\n" + "="*80)
        print("ALL STUDENTS")
        print("="*80)
        for student in self.students.values():
            print(student)
        print("="*80 + "\n")
    
    def search_student(self, student_id):
        if student_id in self.students:
            print("\n" + "-"*80)
            print("STUDENT FOUND")
            print("-"*80)
            print(self.students[student_id])
            print("-"*80 + "\n")
            return self.students[student_id]
        else:
            print(f"Student with ID {student_id} not found.")
            return None
    
    def update_student(self, student_id, name=None, age=None, grade=None, email=None):
        if student_id not in self.students:
            print(f"Student with ID {student_id} not found.")
            return False
        
        student = self.students[student_id]
        if name:
            student.name = name
        if age:
            student.age = age
        if grade:
            student.grade = grade
        if email:
            student.email = email
        
        print(f"Student {student_id} updated successfully!")
        return True
    
    def delete_student(self, student_id):
        if student_id in self.students:
            student_name = self.students[student_id].name
            del self.students[student_id]
            print(f"Student {student_name} (ID: {student_id}) deleted successfully!")
            return True
        else:
            print(f"Student with ID {student_id} not found.")
            return False
    
    def get_student_count(self):
        return len(self.students)


def display_menu():
    print("\n" + "="*50)
    print("STUDENT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Show Total Students")
    print("7. Exit")
    print("="*50)


def main():
    sms = StudentManagementSystem()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            print("\n--- Add New Student ---")
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Name: ").strip()
            age = input("Enter Age: ").strip()
            grade = input("Enter Grade: ").strip()
            email = input("Enter Email: ").strip()
            
            sms.add_student(student_id, name, age, grade, email)
        
        elif choice == '2':
            sms.view_all_students()
        
        elif choice == '3':
            print("\n--- Search Student ---")
            student_id = input("Enter Student ID to search: ").strip()
            sms.search_student(student_id)
        
        elif choice == '4':
            print("\n--- Update Student ---")
            student_id = input("Enter Student ID to update: ").strip()
            
            if student_id in sms.students:
                print("Leave blank to keep current value")
                name = input("Enter new Name: ").strip() or None
                age = input("Enter new Age: ").strip() or None
                grade = input("Enter new Grade: ").strip() or None
                email = input("Enter new Email: ").strip() or None
                
                sms.update_student(student_id, name, age, grade, email)
            else:
                print(f"Student with ID {student_id} not found.")
        
        elif choice == '5':
            print("\n--- Delete Student ---")
            student_id = input("Enter Student ID to delete: ").strip()
            confirm = input(f"Are you sure you want to delete student {student_id}? (yes/no): ").strip().lower()
            
            if confirm == 'yes':
                sms.delete_student(student_id)
            else:
                print("Deletion cancelled.")
        
        elif choice == '6':
            count = sms.get_student_count()
            print(f"\nTotal Students: {count}")
        
        elif choice == '7':
            print("\nThank you for using the Student Management System!")
            break
        
        else:
            print("\nInvalid choice! Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()