import hashlib
import getpass

users = {}

def register():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed_password
    
    print("Registration successful.")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    if username in users and users[username] == hashed_password:
        print("Login successful.")
        return True
    else:
        print("Invalid username or password.")
        return False

def secured_page():
    if login():
        print("Welcome to the secured page.")
    else:
        print("Access denied.")

def main():
    print("1. Register")
    print("2. Login")
    print("3. Secured Page")
    print("4. Quit")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            secured_page()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()