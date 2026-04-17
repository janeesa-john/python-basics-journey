# Program to find the largest number in a list

number = input("Enter numbers: ").split()
l = []
for num in number:
    l.append(int(num))
largest = l[0]
for num in l:
    if num > largest:
        largest = num
print("Largest number: ",largest)