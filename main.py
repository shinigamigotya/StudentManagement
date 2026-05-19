import student
import marks
import attendance

def main():
    print("===================================")
    print("     Student Management System     ")
    print("===================================")
    
    # Calling functions from the imported modules
    student.student_info()
    print("-----------------------------------")
    marks.marks()
    print("-----------------------------------")
    attendance.attendance()
    print("===================================")

if __name__ == "__main__":
    main()
