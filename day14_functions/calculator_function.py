# Calculator program using functions to perform addition and subtraction

def calculator(a,b):
    add = a + b
    diff = a - b
    return add, diff

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
sum_result, diff_result = calculator(num1,num2)
print("Sum: ",sum_result)
print("Difference: ", diff_result)