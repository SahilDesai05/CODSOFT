import time

def start_calculator():
    print("--- MY SIMPLE CALCULATOR ---")
    print("Type 'exit' at any time to quit.")

    while True:
        try:
            # Taking user input as strings first to allow an 'exit' command
            val1 = input("\nEnter first number: ")
            if val1.lower() == 'exit': break
            
            val2 = input("Enter second number: ")
            if val2.lower() == 'exit': break

            # Converting to float for decimal support (e.g., 5.5)
            num1 = float(val1)
            num2 = float(val2)

            print("\nChoose Operation: +, -, *, /")
            op = input("Your choice: ")

            # Standard arithmetic logic
            if op == '+':
                print(f"Result: {num1 + num2}")
            elif op == '-':
                print(f"Result: {num1 - num2}")
            elif op == '*':
                print(f"Result: {num1 * num2}")
            elif op == '/':
                # A 'Human' coder always checks for division by zero!
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error: You can't divide by zero.")
            else:
                print("Invalid operator chosen.")

        except ValueError:
            # This handles cases where the user types 'hello' instead of '5'
            print("Invalid input! Please enter numbers only.")
        
        # Small delay to make the UI feel better
        time.sleep(0.5)

    print("\nThanks for using my calculator!")

if __name__ == "__main__":
    start_calculator()
