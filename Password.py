import string
import random

def generate_password(length, complexity):
    if length < complexity:
        return "Password length should be at least equal to the number of character types selected."

    # Create a pool of characters based on complexity
    char_pools = {
        1: string.ascii_lowercase,
        2: string.ascii_lowercase + string.ascii_uppercase,
        3: string.ascii_lowercase + string.ascii_uppercase + string.digits,
        4: string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    }   
    if complexity not in char_pools:
        return "Invalid complexity level. Please select a level between 1 and 4."

    selected_pool = char_pools[complexity]
    
    # Generate the password using random choices from the selected pool
    password = ''.join(random.choices(selected_pool, k=length))
    
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        print("Select password complexity level:")
        print("1: Lowercase letters only")
        print("2: Lowercase and uppercase letters")
        print("3: Lowercase, uppercase letters, and digits")
        print("4: Lowercase, uppercase letters, digits, and special characters")
        complexity = int(input("Enter complexity level (1-4): "))

        password = generate_password(length, complexity)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter valid numbers for length and complexity level.")

if __name__ == "__main__":
    main()
