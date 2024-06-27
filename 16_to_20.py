# # Python Program to Display the multiplication Table
# def mult(num):
#     for i in range(1,10+1):
#         res=num*i
#         print(f" {num} * {i} = {res}")
# num=int(input())
# mult(num)

# # Python Program to Print the Fibonacci sequence
# def fibo(n):
#     seq=[]
#     a,b=0,1
#     while len(seq)<n:
#         seq.append(a)
#         a,b=b,a+b
#     print(seq,end=" ") 
# nu=int(input())
# fibo(nu)

# Python Program to Check Armstrong Number
def arm(n1):
    n1_str=str(n1)
    n1_digit=len(n1_str)
    sum=0
    for digit in n1_str:
        sum+=int(digit)**n1_digit
    if sum==n1:
        return "Armstrong number"
    else:
        return "no"
numm=int(input())
print(arm(numm))

# Python Program to Find Armstrong Number in an Interval
def find_armstrong_numbers(start, end):
    def is_armstrong(n):
        num_digits = len(str(n))
        sum_of_digits = sum(int(digit) ** num_digits for digit in str(n))
        return sum_of_digits == n
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers
start = int(input())
end = int(input())
armstrong_numbers = find_armstrong_numbers(start, end)
print(f"Armstrong numbers between {start} and {end}:")
print(armstrong_numbers)

# Python Program to Find the Sum of Natural Numbers
def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum
n = 10
result = sum_of_natural_numbers(n)
print(f"The sum of natural numbers up to {n} is {result}")

# Python Program to Print Reverse of a String
def rev(str):
    rev=str[::-1]
    return rev
str=input()
print(rev(str))

# Python Program to Print Sum of First Ten Natural Numbers
def nat():
    sum=0
    for i in range(1,10+1):
        sum+=i
    return sum
print(nat())