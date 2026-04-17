# Append new note to existing text file

note = input("Enter another note: ")

with open("notes.txt", 'a') as file:
    file.write("\n" + note)

print("Note added")