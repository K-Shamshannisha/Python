# Python program to generate a random number
# Method 1: Generating a Random Integer
import random
def random_int(start,end):
    return random.randint(start,end)
start=int(input())
end=int(input())
print(random_int(start,end))

# Method 2: Generating a Random Float
def ran_float(s,e):
    return random.uniform(s,e)
s=float(input())
e=float(input())
print(ran_float(s,e))

# Method 3: Generating a Random Number from a List of Choices
def gen_choice(choices):
    return random.choice(choices)
choices=input().split()
choices=[float(choice) for choice in choices]
print(gen_choice(choices))

# Python program to convert kilometers to miles
# Function to convert kilometers to miles
def kilometers_to_miles(kilometers):
    conversion_factor = 0.621371
    miles = kilometers * conversion_factor
    return miles
# Input distance in kilometers
kilometers = float(input("Enter the distance in kilometers: "))
# Convert to miles
miles = kilometers_to_miles(kilometers)
# Display the result
print(f"{kilometers} kilometers is equal to {miles} miles")

# Python program to convert Celsius to Fahrenheit
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
# Input temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))
# Convert to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)
# Display the result
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")

# Python program to display calendar
import calendar
# Function to display the calendar for a given month and year
def display_calendar(year, month):
    # Create a TextCalendar instance
    cal = calendar.TextCalendar(calendar.SUNDAY)
    # Generate the calendar for the specified month and year
    cal_str = cal.formatmonth(year, month)
    return cal_str
# Input year and month
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
# Ensure the month is valid
if month < 1 or month > 12:
    print("Invalid month. Please enter a month between 1 and 12.")
else:
    # Display the calendar
    cal_output = display_calendar(year, month)
    print(cal_output)

# Python Program to Check if a Number is Positive, Negative or Zero
def posi(n):
    if n>0:
        print("Positive number")
    elif n<0:
        print("Negative number")
    else:
        print("is a zero number")
n=int(input())
print(posi(n))