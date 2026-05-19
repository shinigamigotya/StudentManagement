def mark_attendance(db):
    roll_no = input("Enter the Roll Number of the student: ")
    
    if roll_no in db:
        student_name = db[roll_no]['name']
        status = input(f"Is {student_name} Present or Absent? (P/A): ").strip().upper()
        
        if status == 'P':
            db[roll_no]['attendance'] = "Present"
            print(f"Success: {student_name} marked as Present.")
        elif status == 'A':
            db[roll_no]['attendance'] = "Absent"
            print(f"Success: {student_name} marked as Absent.")
        else:
            print("Error: Invalid input. Please use 'P' for Present or 'A' for Absent.")
    else:
        print("Error: Student not found! Please check the Roll Number.")