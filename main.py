"""
PYSEC ESSENTIAL
CSE1021 - Introduction to Computer Problem Solving and Programming
First-year academic project (Units 1-5 concepts)

Features:
1. Password Strength Checker
2. Password Generator
3. Caesar Cipher Encrypt/Decrypt Tool
4. File Integrity Checker (using hashlib - feature-specific, not a syllabus topic)
5. Prime-based Key Generator (educational only, not secure cryptography)
6. Exit
"""

import hashlib
import random


# ==========================================================
# FEATURE 1: PASSWORD STRENGTH CHECKER
# (Unit 3: Boolean values/operators, if-elif-else, for loop)
# ==========================================================
def password_strength_checker():
    print("\n--- Password Strength Checker ---")
    password = input("Enter a password to check: ")

    length_ok = len(password) >= 7
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    symbols = "!@#$%^&*()-_+=<>?/{}[]~"

    # Check each character using a for loop (Unit 3)
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in symbols:
            has_symbol = True

    # Store results in a dictionary (Unit 5)
    results = {
        "Length (>=7)": length_ok,
        "Uppercase": has_upper,
        "Lowercase": has_lower,
        "Digit": has_digit,
        "Symbol": has_symbol
    }

    print("\nPassword Strength Analysis")
    score = 0
    for check_name in results:
        passed = results[check_name]
        if passed:
            score = score + 1
        print(check_name + ": " + ("Yes" if passed else "No"))

    # Decide strength using if-elif-else (Unit 3)
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    print("Strength: " + strength)
    print("(Note: This is a simple educational check, not a professional security system.)")

# ==========================================================
# FEATURE 2: PASSWORD GENERATOR
# (Unit 3: Loops, String building | Unit 4: random module)
# Builds secure passwords that guaranteed pass Feature 1 checks.
# ==========================================================
import random
import string

def password_generator():
    print("\n--- Password Generator ---")
    
    
    try:
        length = int(input("Enter desired password length (minimum 7): "))
        if length < 7:
            print("Notice: Setting length to default minimum of 7 characters.")
            length = 7
    except ValueError:
        print("Invalid input! Setting default length to 12 characters.")
        length = 12


    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_+=<>?/{}[]~"

    
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    
    all_characters = lowercase + uppercase + digits + symbols
    for _ in range(length - 4):
        password_chars.append(random.choice(all_characters))

    
    random.shuffle(password_chars)

    
    generated_password = "".join(password_chars)

    print("\nGenerated Password: " + generated_password)
    print("Strength Rating: Strong (Passes all 5 criteria)")


# ==========================================================
# FEATURE 3: CAESAR CIPHER
# (Unit 3: Character to Number Conversion using ord()/chr())
# ==========================================================
def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                base = ord('A')
            else:
                base = ord('a')
            # Character to number conversion, shift, then back to character
            new_char = chr((ord(ch) - base + shift) % 26 + base)
            result = result + new_char
        else:
            # Spaces, digits, punctuation stay unchanged
            result = result + ch
    return result


def caesar_decrypt(text, shift):
    # Decryption is just encryption with the opposite shift
    return caesar_encrypt(text, -shift)


def caesar_cipher():
    print("\n--- Caesar Cipher Encrypt/Decrypt ---")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option (1 or 2): ")

    if choice != "1" and choice != "2":
        print("Invalid choice.")
        return

    text = input("Enter the message: ")
    shift_input = input("Enter the shift value (whole number): ")

    if not shift_input.lstrip("-").isdigit():
        print("Invalid shift value. Please enter a whole number.")
        return

    shift = int(shift_input)

    if choice == "1":
        output = caesar_encrypt(text, shift)
        print("Encrypted message: " + output)
    else:
        output = caesar_decrypt(text, shift)
        print("Decrypted message: " + output)


# ==========================================================
# FEATURE 4: FILE INTEGRITY CHECKER
# (hashlib and file reading are feature-specific Python
#  facilities, not core CSE1021 syllabus topics. The overall
#  structure uses functions, if/else and program verification,
#  which are syllabus concepts.)
# ==========================================================
def calculate_file_hash(filepath):
    try:
        file = open(filepath, "rb")
        data = file.read()
        file.close()
        hash_value = hashlib.sha256(data).hexdigest()
        return hash_value
    except FileNotFoundError:
        return None
    except Exception:
        return None


def file_integrity_checker():
    print("\n--- File Integrity Checker ---")
    print("1. Generate Hash")
    print("2. Compare Hash")
    print("3. Back")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        filepath = input("Enter the file path: ")
        hash_value = calculate_file_hash(filepath)
        if hash_value is None:
            print("Error: File not found or could not be read.")
        else:
            print("SHA-256 Hash: " + hash_value)

    elif choice == "2":
        filepath = input("Enter the file path: ")
        current_hash = calculate_file_hash(filepath)
        if current_hash is None:
            print("Error: File not found or could not be read.")
            return
        reference_hash = input("Enter the previously recorded reference hash: ")
        if current_hash == reference_hash.strip():
            print("Result: The file contents appear unchanged.")
        else:
            print("Hash mismatch: The file contents may have changed.")

    elif choice == "3":
        return
    else:
        print("Invalid choice.")


# ==========================================================
# FEATURE 5: PRIME-BASED KEY GENERATOR
# (Unit 4: GCD, prime generation, pseudo-random numbers)
# Educational only - NOT a secure cryptographic key generator.
# ==========================================================
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime(low, high):
    # Keep trying random numbers in range until a prime is found
    attempts = 0
    while attempts < 1000:
        num = random.randint(low, high)
        if is_prime(num):
            return num
        attempts = attempts + 1
    return None  # Safety fallback if no prime found (should not normally happen)


def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def prime_key_generator():
    print("\n--- Educational Prime-Based Key Generator ---")

    prime1 = generate_prime(10, 50)
    prime2 = generate_prime(10, 50)

    # Make sure the two primes are different
    while prime2 == prime1:
        prime2 = generate_prime(10, 50)

    if prime1 is None or prime2 is None:
        print("Error: Could not generate primes. Please try again.")
        return

    gcd_value = calculate_gcd(prime1, prime2)
    random_value = random.randint(1, 100)

    # Simple educational key formed from primes, GCD and a random value
    educational_key = (prime1 * prime2 + random_value) % 1000

    print("Prime 1: " + str(prime1))
    print("Prime 2: " + str(prime2))
    print("GCD of Prime 1 and Prime 2: " + str(gcd_value))
    print("Pseudo-random value: " + str(random_value))
    print("Educational Key: " + str(educational_key))
    print("(This key is for learning purposes only and is not cryptographically secure.)")


# ==========================================================
# MAIN MENU
# (Unit 1: top-down design | Unit 3: while, if-elif-else, break)
# ==========================================================
def main():
    while True:
        print("\n==================================================")
        print("        PYSEC ESSENTIAL")
        print("==================================================")
        print("1. Password Strength Checker")
        print("2. Password Generator")
        print("3. Caesar Cipher Encrypt/Decrypt")
        print("4. File Integrity Checker")
        print("5. Prime-based Key Generator")
        print("6. Exit")
        print("==================================================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            password_strength_checker()
        elif choice == "2":
            password_generator()   
        elif choice == "3":
            caesar_cipher()
        elif choice == "4":
            file_integrity_checker()
        elif choice == "5":
            prime_key_generator()
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()