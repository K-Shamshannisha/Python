# Python program to check if the given number is a Disarium Number
def is_disarium(number):
    # Convert the number to a string to iterate over each digit
    digits = str(number)
    length = len(digits)
    # Calculate the sum of each digit raised to the power of its position
    disarium_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(digits))
    # Check if the sum equals the original number
    return disarium_sum == number
# Input from the user
number = int(input("Enter a number: "))
# Check and display if the number is a Disarium number
if is_disarium(number):
    print(f"{number} is a Disarium number.")
else:
    print(f"{number} is not a Disarium number.")

# Python program to print all disarium numbers between 1 to 100
def calculate_sum_of_powers(number):
    # Convert number to string to iterate through each digit
    digits = str(number)
    length = len(digits)
    sum_powers = 0
    # Calculate sum of powers of digits
    for i in range(length):
        sum_powers += int(digits[i]) ** (i + 1)
    return sum_powers
def print_disarium_numbers():
    disarium_numbers = []
    for num in range(1, 101):
        if num == calculate_sum_of_powers(num):
            disarium_numbers.append(num)
    print("Disarium numbers between 1 and 100:")
    print(disarium_numbers)
# Call the function to print Disarium numbers
print_disarium_numbers()

# Python program to check if the given number is Happy Number
def is_happy_number(number):
    def get_next(num):
        next_num = 0
        while num > 0:
            num, digit = divmod(num, 10)
            next_num += digit ** 2
        return next_num
    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = get_next(number)
    return number == 1
# Input from the user
number = int(input("Enter a number: "))
# Check if the number is a Happy Number
if is_happy_number(number):
    print(f"{number} is a Happy Number.")
else:
    print(f"{number} is not a Happy Number.")

# Python program to print all happy numbers between 1 and 100
def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit)**2 for digit in str(num))
    return num == 1
def print_happy_numbers(limit):
    happy_numbers = []
    for num in range(1, limit + 1):
        if is_happy_number(num):
            happy_numbers.append(num)
    print("Happy numbers between 1 and", limit, "are:", happy_numbers)
# Finding happy numbers between 1 and 100
print_happy_numbers(100)

# Python program to determine whether the given number is a Harshad Number
def is_harshad_number(num):
    # Calculate the sum of the digits of the number
    sum_of_digits = sum(int(digit) for digit in str(num))
    # Check if the number is divisible by the sum of its digits
    return num % sum_of_digits == 0
# Input: the number to be checked
number = int(input("Enter a number: "))
# Check if the given number is a Harshad number
if is_harshad_number(number):
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")

# Python program to print all pronic numbers between 1 and 100
def is_pronic_number(num):
    # Check if the number is a product of two consecutive integers
    for i in range(1, int(num**0.5) + 1):
        if i * (i + 1) == num:
            return True
    return False
def print_pronic_numbers(limit):
    pronic_numbers = []
    for num in range(1, limit + 1):
        if is_pronic_number(num):
            pronic_numbers.append(num)
    print(f"Pronic numbers between 1 and {limit} are:", pronic_numbers)
# Finding pronic numbers between 1 and 100
print_pronic_numbers(100)

# Python program to print first ten natural numbers.
def print_first_ten_natural_numbers():
    for num in range(1, 11):
        print(num)
# Print the first ten natural numbers
print_first_ten_natural_numbers()

# Python Progran to check an Armstrong number or not
def is_armstrong_number(num):
    # Convert the number to a string to easily iterate over its digits
    digits = str(num)
    num_digits = len(digits)
    # Calculate the sum of the digits each raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == num
# Input: the number to be checked
number = int(input("Enter a number: "))
# Check if the given number is an Armstrong number
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
