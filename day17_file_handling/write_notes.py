# Write user note to a text file using file handling

note = input("Enter a note: ")

with open("notes.txt",'w') as file:
    file.write(note)

print("Note saved successfully")