import re

def user_info(name, email):

    if(name.strip() == ""):
        print("Invalid Input, You entered an empty entry.")
    elif(not name.isalpha()):
        print("Invalid Input, Please enter alphapetic character only.")

    if('@' not in email or "." not in email):
        print("Invalid Input, Please enter a valid email containing @ and .")
    else:
        parts = email.split('@')
        if len(parts) == 2:
            user = parts[0]
            domain = parts[1].split('.')
            if len(domain) == 2:
                service = domain[0]
                org = domain[1]
                if user and service and org:
                    print(f"Hello {name}, this is your email address {email}")
            else:
                print("The '.' should be after the '@'")
        else:
            print("The Email format should be (name@service.organization)")

def user_info_error_handel(name, email):
    validate_username(name)
    validate_email(email)
    print(f"Hello, {name}, your email is: {email}")

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