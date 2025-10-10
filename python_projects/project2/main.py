import os

History = "history.txt"

def show_history():
    if os.path.exists(History):
        with open(History, "r") as f:
            content = f.read()
            if content.strip() == "":
                print("No history found.")
            else:
                print("\nCalculation History:\n")
                print(content)
    else:
        print("No history file found.")

def msg_print():
    print("\nWelcome to the Terminal-Based Calculator")
    print("Enter 'q' to quit the program")
    print("Enter 's' to start the calculation")
    print("Enter 'h' to see the history")
    print("Enter 'c' to clear the history")

def dummy():
    print("Operators included: +, -, *, /")
    print("Hit enter after entering each input (e.g., 8 [enter] + [enter] 4)")


msg_print()

while True:
    user = input("\nEnter your choice: ").lower()

    if user == "q":
        print("Exiting... Goodbye!")
        break

    elif user == "s":
        dummy()
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator: ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Error: Division by zero not allowed.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator!")
                continue

            print(f"Result: {num1} {operator} {num2} = {result}")
            with open(History, "a") as f:
                f.write(f"{num1} {operator} {num2} = {result}\n")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

    elif user == "h":
        show_history()

    elif user == "c":
        open(History, "w").close()
        print("History cleared successfully.")

    else:
        print("Invalid choice. Please try again.")

    msg_print()
