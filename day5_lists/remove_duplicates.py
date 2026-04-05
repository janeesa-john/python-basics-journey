#Remove duplicates

duplicate = list(map(int,input("Enter numbers: ").split()))
unique = []
for num in duplicate:
    if num not in unique:
        unique.append(num)
print("Unique numbers: ",unique)
