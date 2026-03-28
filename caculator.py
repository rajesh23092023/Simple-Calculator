def calculator():
    print("--- Simple Calculator ---")
    
    while True:
        print("Select operation:")
        print("1. Add      2. Subtract")
        print("3. Multiply 4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")
        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result = ", num1 + num2)
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result = ", num1 - num2)
        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result = ", num1 * num2)
        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result = ", num1 / num2)
        elif choice == '5':
            print("Exit!!!")
            break

        else:
            print("Invalid input. Please select a valid operation.")

calculator()
