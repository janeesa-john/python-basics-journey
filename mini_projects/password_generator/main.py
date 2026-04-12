# Password Generator


import random
import string

print("🔐 Password Generator")

while True:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Enter a valid length")
        continue

    chars = string.ascii_letters + string.punctuation + string.digits
    password = ''

    for i in range(length):
        password+= random.choice(chars)

    print(f"Generated password: {password}")

    again = input("Generate again?(yes/no): ").lower()

    if again != 'yes':
        print("Good Bye!")
        break