import random
import string

def generate_password(length):
    """
    Generate a random password of the specified length.
    Includes uppercase, lowercase, digits, and special characters.
    """
    if length < 4:
        print("Password length must be at least 4 to include all character types.")
        return None

    # Character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each category is included
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining length with random choices from all categories
    all_characters = lowercase + uppercase + digits + symbols
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    try:
        # Get desired password length from the user
        length = int(input("Enter the desired password length (minimum 4): "))
        if length < 4:
            print("Error: Password length must be at least 4.")
            return
        
        # Generate and display the password
        password = generate_password(length)
        if password:
            print(f"\nYour generated password is: {password}")

    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Run the password generator
if __name__ == "__main__":
    main()
