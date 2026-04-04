#Palindrome check

word = input("Enter a word: ")
rev = ""
for i in word:
    rev = i + rev
if word==rev:
    print(word,"is a palindrome")
else:
    print(word,"not a palindrome")
