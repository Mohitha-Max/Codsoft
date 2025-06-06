import random
import string

def generate_password(length):
    if length<4:
        return "Password length should be alteast 4 for better security "
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    user_input = int(input("Enter the desired password length:"))
    generated_password = generate_password(user_input)
    print("Generated password:", generated_password)

except ValueError:
    print("Please enter a valid number!")