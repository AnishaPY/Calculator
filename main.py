def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    if num2 !=0 :
        return num1 / num2
    else:
        print("Invalid Number")

def calculator():
    print("Welcome to Calculator")
    while True:
        # Display menu
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")
        if choice == '5':
            print("Exit from the calculator. Goodbye!")
            break
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {sub(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {mul(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {div(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid operation.")
calculator()










