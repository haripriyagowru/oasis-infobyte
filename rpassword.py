import random
import string

def generate_password(length):
    # Define the character sets for your password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Specify the length of the password you want
password_length = int(input("Enter the lenght of password:"))  

# Generate and print a random password
password = generate_password(password_length)
print("Random Password:", password)