ch="yes"
while ch.lower()=="yes":
    print("Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        result = n1 + n2
        print("addition of two number =", result)

    elif choice == 2:
        result = n1 - n2
        print("subraction of number =", result)

    elif choice == 3:
        result = n1 * n2
        print("multiplication of two number =", result)

    elif choice == 4:
        if n2 != 0:
            result = n1 / n2
            print("division of two number =", result)
        else:
            print("Error: Division by zero is not allowed")

    else:
        print("Invalid choice!")

    ch=input("do you want to contnue?")
