#Count frequency

numbers = list(map(int, input("Enter numbers: ").split()))
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num]=1
print("Frequency: ",frequency)
