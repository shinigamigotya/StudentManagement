def add_marks(db):
    roll_no = input("Enter the Roll Number of the student: ")
    
    if roll_no in db:
        student_name = db[roll_no]['name']
        score = input(f"Enter the marks for {student_name}: ")
        db[roll_no]['marks'] = score
        print(f"Success: Marks updated for {student_name}.")
    else:
        print("Error: Student not found! Please check the Roll Number or add the student first.")