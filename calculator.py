def calculator():
    print("*************  Welcome to the basic Calculator  ************")
    
    while True:
        print("1. Multiplication\n2. Division\n3. Addition\n4. Subtraction\n5. Quit")
        choice = int(input("Please make a choice (1/2/3/4/5):"))
        
        if choice == 5:
            print("Exiting the calculator. Goodbye!")
            break  # Exit the loop and end the program
        
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        
        if choice == 1:
            result = num1 * num2
            print("Result is:", result)
        elif choice == 2:
            if num2 == 0:
                print("Error: Division by zero")
            else:
                result = num1 / num2
                print("Result is:", result)
        elif choice == 3:
            result = num1 + num2
            print("Result is:", result)
        elif choice == 4:
            result = num1 - num2
            print("Result is:", result)
        else:
            print("Invalid Choice")

calculator()
