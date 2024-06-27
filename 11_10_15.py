# Python Program to Check if a Number is Odd or Even
def odd_even(n):
    if n%2==0:
        return "Even number"
        # print("Even number")
    else:
        print("Odd number")
num=int(input())
res=odd_even(num)
print(res)
print(odd_even(num))

# Python Program to Check Leap Year
def leap_year(n):
    if n%4==0:
        if  n%100==0 :
            if  n%400==0:
                return "leap year"
            else:
                return "not leap year"
        else:
            return "leap year"
    else:
        return "not a leap year"
num=int(input())
print(leap_year(num))

# Python Program to Check Prime Number
def prime_num(n1):
    if n1<=1:
        return "not prime"
    for i in range(2,int(n1**0.5)+1):
        if n1%i==0:
            return "not prime"
        else:
            return "prime"
n1=int(input())
print(prime_num(n1))

# Python Program to Print all Prime Numbers in an Interval
def print_primes(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)
start=int(input())
end=int(input())
print_primes(start, end)

# Python Program to Find the Factorial of a Number
def fact(a):
    result=1
    for i in range(1,a+1):
        result*=i
    return result
a=int(input())
print(fact(a))
