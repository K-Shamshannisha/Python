# Python Program to Find LCM
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return a*b//gcd(a,b)
a=int(input())
b=int(input())
print(lcm(a,b))

# Python Program to Find HCF
def gcd1(a,b):
    while b:
        a,b=b,a%b
    return a
num1=int(input())
num2=int(input())
print(gcd1(num1,num2))

# Python Program to Convert Decimal to Binary, Octal and Hexadecimal
def convert_number(decimal_number):
    # Convert to binary
    binary_representation = bin(decimal_number)
    # Convert to octal
    octal_representation = oct(decimal_number)
    # Convert to hexadecimal
    hexadecimal_representation = hex(decimal_number)
    return binary_representation, octal_representation, hexadecimal_representation
# Input from the user
decimal_number = int(input("Enter a decimal number: "))
# Conversion
binary, octal, hexadec = convert_number(decimal_number)
# Display the results
print(f"Decimal: {decimal_number}")
print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexadec}")

# Python Program To Find ASCII value of a character
def find_ascii_value(character):
    # Get the ASCII value using the ord() function
    ascii_value = ord(character)
    return ascii_value
# Input from the user
character = input("Enter a character: ")
# Ensure the input is a single character
if len(character) != 1:
    print("Please enter exactly one character.")
else:
    # Find and display the ASCII value
    ascii_value = find_ascii_value(character)
    print(f"The ASCII value of '{character}' is {ascii_value}.")

# Python Program to Make a Simple Calculator
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice (1/2/3/4): ")
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input. Please enter a number between 1 and 4.")
# Run the calculator
calculator()

# Python Program to Display Calendar
import calendar
def display_calendar(year, month):
    # Create a TextCalendar instance
    cal = calendar.TextCalendar(calendar.SUNDAY)
    # Generate the month's calendar as a multi-line string
    month_calendar = cal.formatmonth(year, month)
    # Print the calendar
    print(month_calendar)
# Input from the user
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
# Ensure the month is within valid range
if 1 <= month <= 12:
    display_calendar(year, month)
else:
    print("Invalid month. Please enter a number between 1 and 12.")

# Python Program to Display Fibonacci Sequence Using Recursion
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def display_fibonacci_sequence(terms):
    sequence = []
    for i in range(1, terms + 1):
        sequence.append(fibonacci(i))
    return sequence
# Input from the user
terms = int(input("Enter the number of terms: "))
# Ensure the input is a positive integer
if terms <= 0:
    print("Please enter a positive integer.")
else:
    # Display the Fibonacci sequence
    fibonacci_sequence = display_fibonacci_sequence(terms)
    print("Fibonacci sequence:")
    for num in fibonacci_sequence:
        print(num, end=" ")

# Python Program to Find Factorial of Number Using Recursion
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Input from the user
number = int(input("Enter a number: "))
# Calculate factorial and display the result
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")

# Python Program to Calculate the Power of a Number
def power(base, exponent):
    # Base case: exponent is 0
    if exponent == 0:
        return 1
    # If exponent is negative, convert to positive and invert the result
    elif exponent < 0:
        return 1 / power(base, -exponent)
    # Recursive case: exponent is positive
    else:
        return base * power(base, exponent - 1)
# Input from the user
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
# Calculate the power and display the result
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}.")




