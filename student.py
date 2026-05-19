def add_student(db):
    roll_no = input("Enter Student Roll Number: ")
    
    if roll_no in db:
        print("Error: A student with this Roll Number already exists!")
    else:
        name = input("Enter Student Name: ")
        db[roll_no] = {
            "name": name, 
            "marks": "Not Assigned", 
            "attendance": "Not Marked"
        }
        print(f"Success: Student '{name}' added to the system!")

def view_students(db):
    if not db:
        print("The database is currently empty. Please add a student first.")
        return
        
    print("\n--- Current Student Records ---")
    for roll_no, info in db.items():
        print(f"Roll No: {roll_no} | Name: {info['name']} | Marks: {info['marks']} | Attendance: {info['attendance']}")
    print("-------------------------------")