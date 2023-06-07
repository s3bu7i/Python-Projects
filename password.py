import re

def check_password_strength(password):

    strong_password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    # Check if the password meets the criteria
    if re.match(strong_password_regex, password):
        return "Strong"
    else:
        return "Weak"

# Get user input
password_input = input("Enter your password: ")

# Check the password strength
password_strength = check_password_strength(password_input)
print("Password Strength:", password_strength)
