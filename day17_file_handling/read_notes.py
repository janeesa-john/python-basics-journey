# Read and display content from notes.txt file

with open("notes.txt", 'r') as file:
    data = file.read()

print(data)