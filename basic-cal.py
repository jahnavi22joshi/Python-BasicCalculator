# Basic Calculator in Python

def add(x, y):
    """Addition function"""
    return x + y

def subtract(x, y):
    """Subtraction function"""
    return x - y

def multiply(x, y):
    """Multiplication function"""
    return x * y

def divide(x, y):
    """Division function"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    """Power function"""
    return x ** y

def percentage(x, y):
    """Percentage function - x% of y"""
    return (x * y) / 100

def display_menu():
    """Display calculator menu"""
    print("\n" + "="*40)
    print("         BASIC CALCULATOR")
    print("="*40)
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (**)")
    print("6. Percentage (%)")
    print("7. Exit")
    print("="*40)

def get_numbers():
    """Get two numbers from user input"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return None, None

def main():
    """Main calculator function"""
    print("Welcome to Basic Calculator!")
    
    while True:
        display_menu()
        
        # Get user choice
        choice = input("Enter choice (1-7): ")
        
        if choice == '7':
            print("Thank you for using the calculator!")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            # Get numbers from user
            num1, num2 = get_numbers()
            
            if num1 is None or num2 is None:
                continue
            
            # Perform calculation based on choice
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            elif choice == '5':
                result = power(num1, num2)
                operation = "**"
            elif choice == '6':
                result = percentage(num1, num2)
                print(f"\n{num1}% of {num2} = {result}")
                continue
            
            # Display result
            if isinstance(result, str):  # Error message
                print(f"\n{result}")
            else:
                print(f"\n{num1} {operation} {num2} = {result}")
        
        else:
            print("Invalid input! Please select a valid option (1-7).")
        
        # Ask if user wants to continue
        continue_calc = input("\nDo you want to perform another calculation? (y/n): ")
        if continue_calc.lower() != 'y':
            print("Thank you for using the calculator!")
            break

# Run the calculator
if __name__ == "__main__":
    main()

# Alternative: Simple Single Operation Calculator
def simple_calculator():
    """A simpler version for beginners"""
    print("\n" + "="*30)
    print("    SIMPLE CALCULATOR")
    print("="*30)
    
    try:
        # Get input from user
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        # Perform calculation
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error! Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operator!")
            return
        
        print(f"\n{num1} {operator} {num2} = {result}")
        
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

# Uncomment the line below to run the simple version instead
# simple_calculator()