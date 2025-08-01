# login.py

# Predefined username and password
USERNAME = "admin"
PASSWORD = "1234"

# Ask for user input
input_username = input("Enter username: ")
input_password = input("Enter password: ")

# Check credentials
if input_username == USERNAME and input_password == PASSWORD:
    print("✅ Login successful!")
else:
    print("❌ Invalid username or password.")

