# Program to reverse a string using slicing

s = input("Enter a word: ")
rev = ""

for i in s:
    rev = i + rev

print(rev)