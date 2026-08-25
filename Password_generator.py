import random
import string

print("PASSWORD GENERATOR")

while True:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length should be at least 4.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated Password:", password)

    again = input("Do you want to generate another password? (yes/no): ")

    if again.lower() == "no":
        print("Thank you!")
        break
