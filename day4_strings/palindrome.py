# Program to check whether a string is a palindrome

word = input("Enter a word: ")
rev = ""
for i in word:
    rev = i + rev
if word==rev:
    print(word,"is a palindrome")
else:
    print(word,"not a palindrome")
