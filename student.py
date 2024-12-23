from icecream import ic 
import os  # ייבוא מודול os
import platform  # ייבוא מודול platform

# בודק אם מדובר במערכת הפעלה macOS
if platform.system() == "Darwin":
    os.system('clear')  # הפקודה לניקוי המסך במאק
else:
    print("המערכת אינה macOS")

students = []

# פונקציה להצגת תפריט
def menu():
    print("\np - display all students")
    print("f - find a student")
    print("a - add a new student")
    print("d - delete a student")
    print("x - exit")
    return input("your selection: ")

# פונקציה להוספת תלמיד
def add_student():
    name = input("Enter the student's name: ")
    email = input("Enter the student's email: ")
    students.append({"name": name, "email": email})
    print(f"Student {name} added.")

# פונקציה למחיקת תלמיד
def delete_student():
    name = input("Enter the name of the student to delete: ")
    found = False
    for student in students:
        if student['name'] == name:
            students.remove(student)
            print(f"Student {name} has been deleted.")
            found = True
            break
    if not found:
        print(f"Student {name} not found.")

# פונקציה לחיפוש תלמיד
def find_student():
    name = input("Enter the student's name to find: ")
    found = False
    for student in students:
        if student['name'] == name:
            print(f"Student found: {student}")
            found = True
            break
    if not found:
        print(f"Student {name} not found.")

# פונקציה להדפסת כל התלמידים
def display_all_students():
    if students:
        print("\nAll students:")
        for student in students:
            print(f"Name: {student['name']}, Email: {student['email']}")
    else:
        print("No students available.")

if __name__ == "__main__":  # פונקצית כניסה
    while True:
        choice = menu()  # הצגת תפריט
        if choice == "x":
            print("Exiting the program.")
            break
        elif choice == "p":
            display_all_students()  # הצגת כל התלמידים
        elif choice == "f":
            find_student()  # חיפוש תלמיד
        elif choice == "a":
            add_student()  # הוספת תלמיד
        elif choice == "d":
            delete_student()  # מחיקת תלמיד
        else:
            print("Wrong selection, please try again.")
ic(students)  # הדפסת רשימת התלמידים