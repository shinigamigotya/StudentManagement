import student
import marks
import attendance

# This dictionary acts as our shared database
students_db = {}

def main():
    while True:
        print("\n===================================")
        print("     Student Management System     ")
        print("===================================")
        print("1. Add a New Student")
        print("2. Add Student Marks")
        print("3. Mark Student Attendance")
        print("4. View All Student Records")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            student.add_student(students_db)
        elif choice == '2':
            marks.add_marks(students_db)
        elif choice == '3':
            attendance.mark_attendance(students_db)
        elif choice == '4':
            student.view_students(students_db)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()