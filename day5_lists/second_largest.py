# Program to find the second largest number in a list

l = list(map(int,input("Enter numbers: ").split()))
largest = float('-inf')
sec_largest = float('-inf')
for num in l:
    if num > largest:
        sec_largest = largest
        largest = num
    elif num != largest and num > sec_largest:
        sec_largest = num
if sec_largest == float('-inf'):
    print("No second largest")
else:
    print("Second largest: ",sec_largest)