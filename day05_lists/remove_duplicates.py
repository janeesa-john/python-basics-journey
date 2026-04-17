# Program to remove duplicate elements from a list

duplicate = list(map(int,input("Enter numbers: ").split()))
new = []
for num in duplicate:
    if num not in new:
        new.append(num)
print("New list: ",new)
