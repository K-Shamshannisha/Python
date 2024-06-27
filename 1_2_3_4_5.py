# Python program to print "Hello Python"
print("Hello Python")

# Python program to do arithmetical operations
a=int(input())
b=int(input())
print("add:",a+b)
print("sub:",a-b)
print("mul:",a*b)
print("div:",a/b)
print("mod:",a%b)
print("float_div:",a//b)
print("exponent:",a**b)

# Python program to find the area of a triangle
import math
def area_triangle(a,b,c):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

a=int(input())
b=int(input())
c=int(input())
print("area:",area_triangle(a,b,c))

# Python program to solve quadratic equation
import math
# Function to solve the quadratic equation
def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if the discriminant is positive, zero, or negative
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        # One real root
        root = -b / (2 * a)
        return root,
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2
# Input coefficients a, b, and c
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
# Ensure a is not zero for it to be a quadratic equation
if a == 0:
    print("Coefficient 'a' cannot be zero in a quadratic equation.")
else:
    # Solve the quadratic equation
    roots = solve_quadratic(a, b, c)
    # Display the results
    if len(roots) == 1:
        print(f"The equation has one real root: {roots[0]}")
    else:
        print(f"The equation has two roots: {roots[0]} and {roots[1]}")


# Python program to swap two variables
# METHOD 1:USING TUPLE UNpacking:Tuple Unpacking: This method uses Python's ability to unpack tuples. It is the simplest and most Pythonic way to swap two variables.
# Function to swap two variables
def swap_using_tuple(a, b):
    a, b = b, a
    return a, b
# Input two variables
x = input("Enter the first variable: ")
y = input("Enter the second variable: ")
# Swap the variables
x, y = swap_using_tuple(x, y)
# Display the results
print(f"After swapping: x = {x}, y = {y}")

# METHOD 2:Temporary Variable: This method uses a temporary variable to hold the value of one variable while the swap occurs. It is a straightforward approach.
# Function to swap two variables using a temporary variable
def swap_using_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b
# Input two variables
x = input("Enter the first variable: ")
y = input("Enter the second variable: ")
# Swap the variables
x, y = swap_using_temp(x, y)
# Display the results
print(f"After swapping: x = {x}, y = {y}")

# METHOD 3:Arithmetic Operations: This method uses arithmetic operations to swap variables without needing a temporary variable. It only works for numeric values.
# Function to swap two variables using arithmetic operations
def swap_using_arithmetic(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b
# Input two variables
x = float(input("Enter the first variable: "))
y = float(input("Enter the second variable: "))
# Swap the variables
x, y = swap_using_arithmetic(x, y)
# Display the results
print(f"After swapping: x = {x}, y = {y}")

# METHOD 4:Bitwise XOR: This method uses the bitwise XOR operation to swap integer values without a temporary variable. It is a low-level approach and only works with integers.
# Function to swap two variables using bitwise XOR
def swap_using_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
# Input two variables
x = int(input("Enter the first variable: "))
y = int(input("Enter the second variable: "))
# Swap the variables
x, y = swap_using_xor(x, y)
# Display the results
print(f"After swapping: x = {x}, y = {y}")



