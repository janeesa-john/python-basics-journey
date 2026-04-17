# Program to perform basic calculator operations

print("Calculator")
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
print("Choose operation: ")
print("1.Add\n2.Subtract\n3.Multiply\n4.Divide")

choice = input("Enter the choice(1/2/3/4): ")
if choice =='1':
    print(f"{num1}+{num2}= {num1+num2}")
elif choice == '2':
    print(f"{num1}-{num2}= {num1 - num2}")
elif choice == '3':
    print(f"{num1}*{num2}= {num1 * num2}")
elif choice == '4':
    if num2!=0:
        print(f"{num1}/{num2}= {num1 / num2}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")