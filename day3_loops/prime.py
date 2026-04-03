#Prime number check

n = int(input("Enter a number: "))
if n<=1:
    print("Not Prime")
else:
    for num in range(2,n):
        if n%num==0:
            print("Not prime")
            break
    else:
        print("Prime")

