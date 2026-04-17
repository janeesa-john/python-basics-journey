note = input("Enter a note: ")

with open("notes.txt",'w') as file:
    file.write(note)

print("Note saved successfully")