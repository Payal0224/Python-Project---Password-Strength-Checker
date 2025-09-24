import re 

# Password strength check conditions:
# min 8 characters, digits, uppercase, lowercase, special characters 

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    if not any(char.isdigit() for char in password):
        return "Weak: Password must include at least one number."
    
    if not any(char.isupper() for char in password):
        return "Weak: Password must include at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Weak: Password must include at least one lowercase letter."
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Medium: Add special characters to make your password stronger."
    
    return "Strong: Your password is secure!"


def password_checker():
    print("Welcome to the password strength checker")

    while True:
        password = input("Enter your Password (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Thank you for using this tool!")
            break

        result = check_password_strength(password)
        print(result)


# Run the password checker tool
if __name__ == "__main__":
    password_checker()
