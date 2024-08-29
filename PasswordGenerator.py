import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    while True:
        try:
            # Prompt the user to enter the desired length of the password
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Password length must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    # Generate and print the password
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
