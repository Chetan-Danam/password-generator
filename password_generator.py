import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    """Generate a customizable password based on user-defined criteria."""
    
    # Define character sets
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Create the pool of characters based on user choices
    character_pool = ""
    if use_lowercase:
        character_pool += lower_chars
    if use_uppercase:
        character_pool += upper_chars
    if use_digits:
        character_pool += digits
    if use_special_chars:
        character_pool += special_chars

    # Ensure that there are enough characters in the pool for password generation
    if not character_pool:
        raise ValueError("At least one character set must be selected!")

    # Generate password
    password = ''.join(random.choice(character_pool) for _ in range(length))

    return password

def get_user_input():
    """Prompt the user for password criteria."""
    try:
        length = int(input("Enter password length (min 8 characters): "))
        if length < 8:
            print("Password length must be at least 8 characters.")
            return None

        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

        # Generate password
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    get_user_input()
