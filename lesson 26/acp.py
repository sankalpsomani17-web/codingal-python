import secrets
import string
import random

def generate_password(length=12):
    # Define the possible characters
    characters = string.ascii_letters + string.digits
    
    # Securely select random characters
    password_list = [secrets.choice(characters) for _ in range(length)]
    
    # Shuffle the list to ensure extra randomness
    random.shuffle(password_list)
    
    # Join the list into a single string
    return "".join(password_list)

# Generate and print a 12-character password
new_password = generate_password(12)
print(f"Generated Password: {new_password}")