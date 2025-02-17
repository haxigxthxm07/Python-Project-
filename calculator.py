def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Thank you for using the calculator! Goodbye!")
            break

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == "2":
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == "3":
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == "4":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Invalid choice! Please choose a valid operation.")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

