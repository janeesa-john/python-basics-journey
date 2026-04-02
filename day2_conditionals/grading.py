#Grade system

marks = int(input("Enter your marks: "))
if marks < 0 or marks > 100:
    print("Marks Invalid")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Failed")
