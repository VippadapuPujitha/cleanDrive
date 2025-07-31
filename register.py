# registration.py

# Dictionary to hold registered users
users = {}

def register():
    print("=== User Registration ===")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    username = input("Choose a username: ")
    password = input("Choose a password: ")

    if username in users:
        print("❌ Username already exists. Try a different one.")
    else:
        users[username] = {
            "name": name,
            "email": email,
            "password": password
        }
        print("✅ Registration successful!")

def show_users():
    print("\n=== Registered Users ===")
    for user, info in users.items():
        print(f"Username: {user}, Name: {info['name']}, Email: {info['email']}")

# Run the form
register()
show_users()
