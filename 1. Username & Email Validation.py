import re

def validate_username(username):
    try:
        if username == "":
            raise ValueError("Invalid username. The username cannot be empty")
        username = username.strip()
        if not username.isalpha():
            raise ValueError("Invalid username. It must contain only letters (no numbers, spaces, or symbols).")
        print("Username is valid.")
        return True
    except ValueError as ve:
        print(f"Username error: {ve}")
        return False

def validate_email(email):
    try:
        email = email.strip()
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.fullmatch(email_pattern, email):
            raise ValueError("Invalid email format.")
        print("Email is valid.")
        return True
    except ValueError as ve:
        print(f"Email error: {ve}")
        return False

while True:
    username = input("Enter your username: ")
    if validate_username(username):
        break

while True:
    email = input("Enter your email: ")
    if validate_email(email):
        break

print(f"Hello, {username}, your email is: {email}")