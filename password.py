from icecream import ic

def check_password():
    valid_passwords = [123]  # רשימת סיסמאות תקינות
    while True:
        password = input("Enter password : ")
        
		
        # המרת הסיסמה למספר אם אפשר
        try:
            password = int(password)  # המרת הקלט למספר
        except ValueError:
            print("Invalid input. Please enter a numeric password.")
            continue  # אם הקלט לא מספר, נחזור ללולאה

        # אם הסיסמה נכונה
        if password in valid_passwords:
            print("Welcome!")
            break
        else:
            print("Incorrect password. Try again.")

if __name__ == "__main__":
    check_password()




 