#Reverse a string

s = input("Enter a word: ")
rev = ""

for i in s:
    rev = i + rev

print(rev)