# Positive or Negative number:
#  Method 1: Using Brute Force
num = int(input())
if num > 0:
    print('Positive')
elif num < 0:
    print('Negative')
else:
    print('Zero')

# Method 2: Using Nested if-else Statements
num = int(input())
if num>=0:
    if num==0:
        print('Zero')
    else:
        print("Positive")
else:
    print("Negative")

# Method 3: Using ternary operator
num =int(input())
print("Positive" if num>=0 else "Negative")


# Even or Odd number:
# Method 1 : Using Brute Force
num = int(input("Enter a Number:")) 
if num % 2 == 0: 
  print("Given number is Even") 
else: 
  print("Given number is Odd")

# Method 2 : Using Ternary Operator
num = 17
print("Even") if num%2 == 0 else print("Odd")

# Method 3 : Using Bitwise Operators
def isEven(num):
  return not num&1
if __name__ == "__main__":
  num = 13
  if isEven(num):
    print('Even')
  else:
    print('Odd')


#Sum of First N Natural numbers: 
#  Method 1 : Using for Loop
num = int(input())
sum = 0
for i in range(num+1):
  sum+=i
print(sum)

# Method 2 : Using Formula for the Sum of Nth Term
num = int(input())
print(int(num*(num+1)/2))

# Method 3 : Using Recursion
def getSum(num):
  if num == 1:
    return 1
  return num + getSum(num-1)
num = int(input())
print(getSum(num))

# Sum of N natural numbers: 
# Method 1: Using for Loop
number=int(input())
sum = 0
for i in range(number+1):
  sum+=i
print(sum)

# Method 2: Using Formula
number =int(input())
sum = int((number * (number + 1))/2)
print(sum)

# Method 3: Using Recursion
def recursum(number):
  if number == 0:
    return number
  return number + recursum(number-1)
number=int(input()) 
sum = 0
print(recursum(number))

# Sum of numbers in a given range:
# Method 1: Using Brute Force
num1=int(input())
num2 = int(input())
sum = 0
for i in range(num1,num2+1):
  sum+=i
print(sum)

# Method 2: Using the Formula
num1=int(input())
num2 = int(input())
sum = int((num2*(num2+1)/2) - (num1*(num1+1)/2) + num1)
print(sum)

# Method 3: Using Recursion
def recursum(sum,num1,num2):
  if num1 > num2:
    return sum
  return num1 + recursum(sum,num1+1,num2)
num1=int(input())
num2 = int(input())
sum = 0
print(recursum(sum,num1,num2))

# Greatest of two numbers:
# Method 1: Using if-else Statements
num1=int(input())
num2 = int(input())
if num1>num2:
  print(num1)
else:
  print(num2)

# Method 2: Using Ternary Operator
num1=int(input())
num2 = int(input())
print((num1 if num1>num2 else num2))

# Method 3: Using inbuilt max() Function
num1=int(input())
num2 = int(input())
print(max(num1,num2))

# Greatest of the Three numbers:
# Method 1: Using if-else Statements
num1=int(input())
num2 = int(input())
num3=int(input())
max = 0
if num1 >= num2 and num1 >= num3:
  print(num1)
elif num2 >= num1 and num2 >= num3:
  print(num2)
else:
  print(num3)

# Method 2: Using Nested if-else Statements
num1=int(input())
num2 = int(input())
num3=int(input())
max = 0
if num1 >= num2:
    if num1 >= num3:
        print(num1)
elif num2 >= num1:
    if num2 >= num3:
        print(num2)
    else :
        print(num3)

# Method 3: Using Ternary Operator
num1=int(input())
num2 = int(input())
num3=int(input())
max = num1 if num1>num2 else num2
max = num3 if num3>max else max
print(max)


#Leap year or not:
#  Method 1: Using if-else statements 1
year = int(input("Enter a year: ")) 
if (year%400 == 0) or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Method 2: Using if-else statements 2
year =int(input("Enter a year: ")) 
if( ((year % 4 == 0) and (year % 100 != 0)) or (year % 400==0) ):
    print("Leap Year")
else:
    print("Not leap Year")

# Method 3 : Using Ternary Operator
def check_leap(year): 
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) 
year = int(input("Enter a year: ")) 
print(f"{year} is leap year" if check_leap(year) else f"{year} is not leap year")

# Method 4 : Using Calendar Mode
import calendar
year = int(input("Enter a year: "))
if calendar.isleap(year):
    print(year, " is a leap year")
else:
    print(year, "is not a leap year.")

# Method 5 : Using Lamda Function
is_leap_year = lambda year: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, " is a leap year")
else:
    print(year, "is not a leap year.")

# Prime number:
# Method 1: Simple iterative solution
num = int(input()) 
flag = 0
for i in range(2,num):
  if num%i==0:
    flag = 1
    break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")

# Method 2: Optimization by break condition
num = int(input()) 
flag = 0
if num<2:
  flag = 1
else:
  for i in range(2,num):
    if num%i==0:
      flag = 1
      break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")

# Method 3: Optimization by n/2 iterations
num = int(input()) 
flag = 0
if num<2:
  flag = 1
else:
  for i in range(2,int((num/2)+1)):
    if num%i==0:
      flag = 1
      break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")

# Method 4: Optimization by √n
num = int(input()) 
flag = 0
if num<2:
  flag = 1
else:
  for i in range(2,int(pow(num,0.5)+1)):
    if num%i==0:
      flag = 1
      break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")

# Method 5: Optimization by skipping even iteration
num = int(input()) 
flag = 0
if num<2:
  flag = 1
elif num == 2:
  flag = 0
else:
  for i in range(3,int(pow(num,0.5)+1),2):
    if num%i==0:
      flag = 1
      break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")

# Method 6: Basic Recursion technique
num = int(input()) 
def checkPrime(num,iter=2):
  if num == iter:
    return True
  if num%iter==0:
    return False
  if num<2:
    return False
  return checkPrime(num,iter+1)
if checkPrime(num)==True:
  print("Prime")
else:
  print("Not Prime")


#Prime number within a given range:
#  Method 1: Using inner loop Range as [2, number-1].
# python find prime numbers in range 
low=int(input())
high =int(input())
primes = []
for i in range(low, high + 1):
    flag = 0
    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue
    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break
    if flag == 0:
        primes.append(i) 
print(primes)

# Method 2: Using inner loop Range as [2, number/2].
low=int(input())
high =int(input())
primes = [2]
for num in range(low, high + 1):
    flag = 0
    if num < 2:
        flag = 1 
    if num % 2 == 0:
        continue
    iter = 2
    while iter < int(num / 2):
        if num % iter == 0:
            flag = 1
            break
        iter += 1
    if flag == 0:
        primes.append(num)
print(primes)

# Method 3: Using inner loop Range as [2, sqrt(number)].
low=int(input())
high =int(input())
primes = [2, 3]
for num in range(low, high + 1):
    flag = 0
    if num < 2:
        flag = 1
    if num % 2 == 0:
        continue 
    if num % 3 == 0:
        continue   
    iter = 2
    while iter < int(pow(num, 0.5)):
        if num % iter == 0:
            flag = 1
            break
        iter += 1 
    if flag == 0:
        primes.append(num)
print(primes)

# Method 4: Using inner loop Range as [3, sqrt(number), 2].
low=int(input())
high =int(input())
primes = [2, 3]
for num in range(low, high + 1):
    flag = 0
    if num < 2:
        flag = 1
    if num % 2 == 0:
        continue 
    if num % 3 == 0:
        continue
    iter = 3
    while iter < int(pow(num, 0.5)):
        if num % iter == 0:
            flag = 1
            break
        iter += 2
    if flag == 0:
        primes.append(num)
print(primes)


# Sum of digits of a number:
# Method 0: Using String Extraction method
num = input("Enter Number: ")
sum = 0
for i in num:
    sum = sum + int(i)
print(sum)

# Method 1: Using Brute Force
num = input("Enter Number: ")
sum = 0
while num!=0:
	digit = int(num%10)
	sum += digit
	num = num/10
print(sum)

# Method 2: Using Recursion I
num = input("Enter Number: ")
sum = 0
def findSum(num, sum):
    if num == 0:
        return sum
    digit = int(num % 10)
    sum += digit
    return findSum(num / 10, sum)
print(findSum(num, sum))

# Method 3: Using Recursion II
num = input("Enter Number: ")
def findSum(num):
    if num == 0:
        return 0
    return int(num % 10) + findSum(num / 10)
print(findSum(num))

# Method 4: Using ASCII table
num = input("Enter Number: ")
sum = 0
for i in range(len(str(num))):
    # ord methods helps with ASCII
    sum += ord(str(num)[i]) - 48
print(sum)

# Method 5: Using map(), sum() and strip methods
def getSum(n):
    # convert into string
    num_string = str(n)
    # fetch each individual char using strip method
    # find comparable int and store it in map
    # covert it into list
    list_of_number = list(map(int, num_string.strip()))
    print(list_of_number)
    # sum function returns the sum of all items in list
    return sum(list_of_number)
n = int(input("Enter the number: "))
print(getSum(n))

# Method 6: One Line recursive function
def sumDigits(n):
    return 0 if n == 0 else int(n % 10) + sumDigits(int(n / 10)) 
# Driver code
n = int(input("Enter the number: "))
print(sumDigits(n))

# Method 7 : The cool method
n = [int(d) for d in input("Enter the number : ")]
print("the sum of digits is : ", sum(n))


# Reverse of a number :
# Method 1: Using Simple Iteration
num = input()
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10
print(reverse)

# Method 2: Using String Slicing
num = input()
print(str(num)[::-1])

# Method 3: Using Recursion
def recursum(number,reverse):
  if number==0:
    return reverse
  remainder = int(number%10)
  reverse = (reverse*10)+remainder
  return recursum(int(number/10),reverse)
num = input()
reverse = 0
print(recursum(num,reverse))


# Palindrome number:
# Method 1:  Using Simple Iteration.
num = input()
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")

# Method 2: Using String Slicing.
num = input()
reverse = int(str(num)[::-1])
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")

# Method 3: Using Recursion
def recurrev(number, rev):
    if number == 0:
        return rev
    remainder = int(number % 10)
    rev = (rev * 10) + remainder
    return recurrev(int(number / 10), rev)
num = input()
reverse = 0
reverse = recurrev(num, reverse)
print(str(num) + " is: ", end="")
print("Palindrome") if reverse == num else print("Not Palindrome")

# Method 4:  Using Character matching
def checkPalindrome(str):
    # check if str[i] is same as str[len(str) - i - 1]
    # for whole string
    for i in range(0, len(str)):
        # Basically, we are checking i-th character is
        # same as i-th character from the end or not
        if str[i] != str[len(str) - i - 1]:
            return False
    return True
# main function
s = input()
print("Palindrome") if checkPalindrome(s) else print("Not Palindrome")

# Method 5: Using Character matching updated
# we do not need to check the whole string
# only till the mid of string
# as if it palindrome the first half == second half of string when read backwards
def checkPalindrome(str):
    # Run loop from 0 to len/2
    mid = int(len(str) / 2)
    for i in range(0, mid):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True
# main function
s = input() #s = "kayak"
print("Palindrome") if checkPalindrome(s) else print("Not Palindrome")

# Method 6: Using Built-in reversed function
def checkPalindrome(str):
    # using inbuilt reversed function
    reverse = ''.join(reversed(str))
    if str == reverse:
        return True
    return False
# main function
s = input()
print("Palindrome") if checkPalindrome(s) else print("Not Palindrome")

# Method 7:  Building reverse one char at a time
string = input()
# this will automatically generate reverse
rev = ""
for char in string:
    rev = char + rev
print("Palindrome") if string == rev else print("Not Palindrome")
print("string: " + str(string))
print("rev: " + str(rev))

# Method 8: Using Flag and backward reading
string = input()
j = -1
flag = 0
for char in string:
    # char starts from index 0
    # string[j] forces to read from end
    # bcz negative index are read from end
    if char != string[j]:
        flag = 1
        break
    j = j - 1
print(string + " is : ", end="")
print("Not Palindrome") if flag else print("Palindrome")

# Method 9: Bonus using backward slicing
str1 = input()
n = len(str1)
c = []
for i in range(n - 1, -1, -1):
    c.append(str1[i])
rev = "".join(c)
print(str1 + " is: ", end="")
if str1 == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# Armstrong number :
# Method 1: Using Iteration
number = input()
num = number
digit, sum = 0, 0
length = len(str(num))
for i in range(length):
  digit = int(num%10)
  num = num/10
  sum += pow(digit,length)
if sum==number:
  print("Armstrong")
else:
  print("Not Armstrong")

# Method 2: Using Recursion
number = 371
num = number
sum =0
length = len(str(num))
def checkArmstrong(num,length,sum):
  if num==0:
    return sum
  sum+=pow(int(num%10),length)
  return checkArmstrong(num/10,length,sum)
if checkArmstrong(num,length,sum)==number:
  print('Armstrong')
else:
  print("Not Armstrong")


# Armstrong number in a given range : 
# Method 1
low, high = 10, 10000
for n in range(low, high + 1):
    # order of number
    order = len(str(n))
    # initialize sum
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if n == sum:
        print(n, end=", ")

# Method 2
import math
first, second = 150, 10000
def is_Armstrong(val):
    sum = 0
    # this splits the val into its digits
    # example val : 153 will become [1, 5, 3]
    arr = [int(d) for d in str(val)]
    # now we iterate on array items (digits)
    # add these (digits raised to power of len i.e order) to sum
    for i in range(0, len(arr)):
        sum = sum + math.pow(arr[i], len(arr))
    # if sum == val then its armstrong
    if sum == val:
        print(str(val) + ", ", end="")
for i in range(first, second + 1):
    is_Armstrong(i)


# Fibonacci Series upto nth term :
# Method 1: Using Simple Iteration
# Write a program to print fibonacci series upto n terms in python
num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
print()

# Method 2: Using Recursive Function
# Python program to print Fibonacci Series
def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))
num=10
if num <=0:
    print("Please enter a Positive Number")
else:
    print("Fibonacci Series:", end=" ")
for i in range(num):
    print(fibonacciSeries(i), end=" ")

# Method 3: Using direct formulae
 # write a program to print fibonacci series in python
import math
def fibonacciSeries(phi, n):
    for i in range(0, n + 1):
        result = round(pow(phi, i) / math.sqrt(5))
        print(result, end=" ")
num = 10
phi = (1 + math.sqrt(5)) / 2
fibonacciSeries(phi, num)


# Find the Nth Term of the Fibonacci Series :
# Method 1: Using Simple Iteration
# Write a program to print fibonacci series upto n terms in python
num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
print()

# Method 2: Using Recursive Function
# Python program to print Fibonacci Series
def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))
num=10
if num <=0:
    print("Please enter a Positive Number")
else:
    print("Fibonacci Series:", end=" ")
for i in range(num):
    print(fibonacciSeries(i), end=" ")

# Method 3: Using direct formulae:We can use direct formula to find nth term of Fibonacci Series as –
# Fn = {[(√5 + 1)/2] ^ n} / √5
# write a program to print fibonacci series in python
import math
def fibonacciSeries(phi, n):
    for i in range(0, n + 1):
        result = round(pow(phi, i) / math.sqrt(5))
        print(result, end=" ")
num = 10
phi = (1 + math.sqrt(5)) / 2
fibonacciSeries(phi, num)


# Factorial of a number :
# Method 1 (Iterative)
num = 6
fact = 1
# Factorial of negative number doesn't exist
if num < 0:
    print("Not Possible")
else:
    for i in range(1, num+1):
        fact = fact * i
print("Factorial of", num, "is", fact)
# Time complexity: O(N)
# Space complexity: O(1)

# Method 2 (Recursive)
def getFactorial(num):
    if num == 0:
        return 1

    return num * getFactorial(num - 1)
num = 6
fact = getFactorial(num)
print("Factorial of", num, "is", fact)
# Time complexity: O(N)
# Space complexity: O(1)
# Auxiliary Space complexity(Function call stack): O(N)


# Power of a number :
# Method 1: Using Pow() Function
num, power = 3, 2
print(pow(num,power))

# Method 2: Using Simple Iteration
num, power = 3, 2
output = 1
for i in range(power):
  output*=num
print(output)

# Method 3: Using Python Operator
num, power = 3, 2
print(num**power)

# Method 4: Using Recursion
num, power = 3, 2
def powerrecur(num,power):
  if power == 0:
    return 1
  return num * powerrecur(num,power-1)
print(powerrecur(num,power))


# Factor of a number :
# Method 1 : Using [1, number] as the range
# method to print the divisors
def printDivisors(n) :
    i = 1
    while i <= n :
        if (n % i==0) :
            print (i,end=" ")
        i = i + 1
# Driver method
print ("The divisors of 100 are: ")
printDivisors(100)

# Method 2 : Using [1, sqrt(number)] as the range
import math
 
# method to print the divisors
def printDivisors(n) :
    # Note that this loop runs till square root
    i = 1
    while i <= math.sqrt(n):
        if (n % i == 0) :
            # If divisors are equal, print only one
            if (n / i == i) :
                print (i,end=" ")
            else :
                # Otherwise print both
                print (i , int(n/i), end=" ")
        i = i + 1
# Driver method
print ("The divisors of 100 are: ")
printDivisors(100)


# Finding Prime Factors of a number :
# Method 1: Using Simple Iteration
def Prime_Factorial(n):
    if n < 4:
        return n
    arr = []
    while n > 1:
        for i in range(2, int(2+n//2)):
            if i == (1 + n // 2):
                arr.append(n)
                n = n // n
            if n % i == 0:
                arr.append(i)
                n = n // i
                break
    return arr
n = 210
print(Prime_Factorial(n))

# Method 2: Using Recursive Function
def Prime_Factorial(n, arr):
    if n < 4:
        return n
    for i in range(2, int(2+n//2)):
        if i == (1 + n // 2):
            arr.append(n)
            n = 1
            return
        if n % i == 0:
            arr.append(i)
            n = n // i
            Prime_Factorial(n, arr)
            break
    return arr
n = 210
arr = []
print(Prime_Factorial(n, arr))


# Strong number :
# Method 1: Using Simple Iteration
#Using Iteration
n =145
#save the number in another variable
temp=n
sum=0
f=[0]*10
f[0]=1
f[1]=1
for i in range(2,10): #precomputing the factorial value from 0 to 9 and store in the array.
    f[i]=f[i-1]*i
#Implementation
while(temp):
    r=temp%10 #r will have the vale u of the unit digit
    temp=temp//10
    sum+=f[r] #adding all the factorial
if(sum==n):
    print("Yes", n ,"is strong number")
else:
    print("No" , n, "is not a strong number")

# Method 2: Using Recursive Function
#Using Recursion
def Factorial(num):
    if num<=0: 
        return 1 
    else: 
        return num*Factorial(num-1) 
sum=0 
def check_StrongNumber(num): 
    global sum 
    if (num>0):
        fact = 1
        rem = num % 10
        check_StrongNumber(num // 10)
        fact = Factorial(rem)
        sum+=fact
    return sum
num=145
if (check_StrongNumber(num) == num):
    print("Yes",num,"is a strong Number.")
else:
    print("No",num,"is not a strong Number.")


# Perfect number :
# Method 1: Using Simple Iteration I
n = 28
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")

# Method 2: Using Simple Iteration II
num = 28
sum = 0

i = 1
while i < num:
    if num % i == 0:
        sum += i

    i += 1

if sum == num:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")

# Method 3: Using Simple Iteration III
num = 28
sum = 0
for i in range(1, num//2 + 1):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")

# Method 4: Using Recursion
sum_n = 0
def getSumDivisors(num, i):
    global sum_n
    # since, all factors can be found will num/2
    # we will only check in this range
    if i <= num // 2:
        if num % i == 0:
            sum_n = sum_n + i
        i += 1
        # recursively call isPerfect
        getSumDivisors(num, i)
    # returns the sum
    # when i becomes > num/2
    return sum_n
num = 28
if getSumDivisors(num, 1) == num:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")

# Method 5: Using Factors
n = 28
sump = 0
for i in range(1, int(pow(n, 0.5))):
    if n % i == 0:
        # For n : (1, n) will always be pair of divisor
        # acc to def., we must ignore adding num itself as divisor
        # when calculating for perfect number
        if i == 1:
            sump += i
        # Example For 100 (10,10)  will be one pair
        # But, we should add value to the sum just once
        elif i == n / i:
            sump += i
        # add both pairs as divisors
        # For any divisor i, n/i will also be a divisor
        else:
            sump += i + n / i
if sump == n:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")
# Time complexity: O(sqrt(N))
# Space complexity: O(1)


# Perfect Square :
# Algorithm ( Method 1 )
from math import sqrt
def isPerfectSquare(x):
    if x >= 0:
        sr = int(sqrt(x))
        return (sr * sr) == x
    return False
n = 84
if isPerfectSquare(n):
    print("True")
else:
    print("False")

# Algorithm ( Method 2 )
import math
def checkperfectsquare(x):
    if (math.ceil(math.sqrt(n)) ==
            math.floor(math.sqrt(n))):
        print("True")
    else:
        print("False")
n = 49
checkperfectsquare(n)


# Automorphic number : 
# Method 1: Using Modulo Operators
number = 376
square = pow(number, 2)
mod = pow(10, len(str(number)))
# 141376 % 1000
if square % mod == number:
    print("It's an Automorphic Number")
else:
    print("It's not an Automorphic Number")

# Method 2: Short cut
# One line method for automorphic number in python
n = 376
# n^2 = 141376 141376[-3::] = 376
print("YES" if int(str(n**2)[-len(str(n))::]) == n else "No")

# Method 3: Using endswith() method
num = 376
a = str(num)
num1 = num ** 2
b = str(num1)
if b.endswith(a):
    print("It's an Automorphic Number")
else:
    print("It's not an Automorphic Number")


# Harshad number : 
# Method 1: Using Iteration I
n = 21
p=n
l=[]
sum1=0
while(n>0):
    x=n%10
    l.append(x)
    n=n//10
sum1=sum(l)
if(p%sum1==0):
    print("Harshad number")
else:
    print("Not harshad number")

# Method 2: Using Iteration II
n = 21
p=n
sum1=0
while(n>0):
    sum1+=n%10
    n=n//10
if(p%sum1==0):
    print("Harshad number")
else:
    print("Not harshad number")


# Abundant number :
# Method 1: Using Range until Number
n = 12
sum=1 # 1 can divide any number 
for i in range(2,n):
  if(n%i==0):    #if number is divisible by i add the number 
   sum=sum+i
if(sum>n):
  print(n,'is Abundant Number')
else:
  print(n,'is not Abundant Number')

# Method 2: Using Range until Sqrt( Number )
import math
n = 12
sum=1 # 1 can divide any number 
i=2
while(i<=math.sqrt(n)): 
  if(n%i==0): 
#if number is divisible by i add the number 
    if(n//i==i): 
# if quotient is equal to divisor add only one of them 
      sum=sum+i 
    else: 
        sum=sum + i + n/i 
        i=i+1 
    if(sum>n):
        print(n,"is Abundant Number")
    else:
        print(n,"is not Abundant Number")


# Friendly pair : 
# Method 1: Using the Range until Number.
def printDivisors(n, factors) :
    i = 1
    while i <= n :
        if (n % i==0) :
            factors.append(i)
        i = i + 1
    return sum(factors) - n
if __name__ == "__main__": 
  number1, number2 = 6, 28
  if int(printDivisors(number1, [])/number1) == int(printDivisors(number2, [])/number2):
    print("Friendly pair")
  else:
    print("Not a Friendly Pair")

# Method 2: Using the Range until Sqrt( Number )
def printDivisors(n, factors) :
    # Note that this loop runs till square root
    i = 1
    while i <= pow(n,0.5):
        if (n % i == 0) : 
            # If divisors are equal, print only one
            if (n / i == i) :
                factors.append(i)
            else :
                # Otherwise print both
                factors.append(i)
                factors.append(int(n/i))
        i = i + 1
    return sum(factors) - n
if __name__ == "__main__": 
  number1, number2 = 6, 28
  if int(printDivisors(number1, [])/number1) == int(printDivisors(number2, [])/number2):
    print("Friendly pair")
  else:
    print("Not a Friendly Pair")


# 
#Working with Numbers
# 
#  Highest Common Factor(HCF):
# Method 1: Linear Quest to find HCF
num1 = 36
num2 = 60
hcf = 1
for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print("Hcf of", num1, "and", num2, "is", hcf)

# Method 2: Euclidean Algorithm: Repeated Subtraction
num1 = 36
num2 = 60
a = num1
b = num2
while num1 != num2:
    if num1 > num2:
        num1 -= num2
    else:
        num2 -= num1
print("Hcf of", a, "and", b, "is", num1)

# Method 3: Recursive Euclidean Algorithm: Repeated Subtraction
# Recursive function to return HCF of two number
def findHCF(num1, num2):
    # Everything divides 0
    if num1 == 0 or num2 == 0:
        return num1 + num2
    # base case
    if num1 == num2:
        return num1
    # num1>num2
    if num1 > num2:
        return findHCF(num1 - num2, num2)
    else:
        return findHCF(num1, num2 - num1)
num1 = 36
num2 = 60
print("Hcf of", num1, "and", num2, "is", findHCF(num1, num2))

# Method 4: Modulo Recursive Euclidean Algorithm: Repeated Subtraction
# This method improves complexity of repeated subtraction
# By efficient use of modulo operator in euclidean algorithm
def getHCF(a, b):
    return b == 0 and a or getHCF(b, a % b)
num1 = 36
num2 = 60
print("Hcf of", num1, "and", num2, "is", getHCF(num1, num2))

# Method 5: Handling Negative Numbers in HCF 
# This method improves complexity of repeated subtraction
# By efficient use of modulo operator in euclidean algorithm
def getHCF(a, b):
    return b == 0 and a or getHCF(b, a % b)
num1 = -36
num2 = 60
# if user enters negative number, we just changing it to positive
# By definition HCF is the highest positive number that divides both numbers
# -36 & 60 : HCF = 12 (as highest num that divides both)
# -36 & -60 : HCF = 12 (as highest num that divides both)
num1 >= 0 and num1 or -num1
num2 >= 0 and num2 or -num2
print("Hcf of", num1, "and", num2, "is", getHCF(num1, num2))


# Lowest Common Multiple (LCM) : 
# Method 1: A linear way to calculate LCM
num1 = 12
num2 = 14
for i in range(max(num1, num2), 1 + (num1 * num2)):
    if i % num1 == i % num2 == 0:
        lcm = i
        break
print("LCM of", num1, "and", num2, "is", lcm)

# Method 2: Modified interval Linear way
num1 = 12
num2 = 14
for i in range(max(num1, num2), 1 + (num1 * num2), max(num1, num2)):
    if i % num1 == i % num2 == 0:
        lcm = i
        break
print("LCM of", num1, "and", num2, "is", lcm)

# Method 3: Simple usage of HCF calculation to determine LCM
num1 = 12
num2 = 14
# Calculating HCF here
for i in range(1, max(num1, num2)):
    if num1 % i == num2 % i == 0:
        hcf = i
# LCM formula
lcm = (num1*num2)//hcf
print("LCM of", num1, "and", num2, "is", lcm)

# Method 4: Repeated subtraction to calculate HCF and determine LCM
def getHCF(num1, num2):
    while num1!=num2:
        if num1>num2:
            num1-=num2
        else:
            num2-=num1
    return num1
num1 = 12
num2 = 14
# Calculating HCF here
hcf = getHCF(num1, num2)
# LCM formula
lcm = (num1*num2)//hcf
print("LCM of", num1, "and", num2, "is", lcm)

# Method 5: Recursive repeated subtraction to calculate HCF and determine LCM
# Recursive function to return HCF of two number
def getHCF(num1, num2):
    # Everything divides 0
    if num1 == 0 or num2 == 0:
        return num1 + num2
    # base case
    if num1 == num2:
        return num1
    # num1>num2
    if num1 > num2:
        return getHCF(num1 - num2, num2)
    else:
        return getHCF(num1, num2 - num1)
num1 = 12
num2 = 14
# Calculating HCF here
hcf = getHCF(num1, num2)
# LCM formula
lcm = (num1*num2)//hcf
print("LCM of", num1, "and", num2, "is", lcm)

# Method 6: Modulo Recursive repeated subtraction to calculate HCF and determine LCM
def getHCF(a, b):
    if b == 0:
        return a
    else:
        return getHCF(b, a % b)
num1 = 12
num2 = 14
hcf = getHCF(num1, num2)
# LCM formula
lcm = (num1 * num2) // hcf
print("The hcf is :", lcm)


# Greatest Common Divisor :
# Method 1: Linear Quest to find GCD
num1 = 36
num2 = 60
gcd = 1
for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print("GCD of", num1, "and", num2, "is", gcd)

# Method 2: Euclidean Algorithm: Repeated Subtraction
num1 = 36
num2 = 60
a = num1
b = num2
while num1 != num2:
    if num1 > num2:
        num1 -= num2
    else:
        num2 -= num1
print("GCD of", a, "and", b, "is", num1)

# Method 3: Recursive Euclidean Algorithm: Repeated Subtraction
# Recursive function to return GCD of two number
def findGCD(num1, num2):
    # Everything divides 0
    if num1 == 0 or num2 == 0:
        return num1 + num2
    # base case
    if num1 == num2:
        return num1
    # num1>num2
    if num1 > num2:
        return findGCD(num1 - num2, num2)
    else:
        return findGCD(num1, num2 - num1)
num1 = 36
num2 = 60
print("GCD of", num1, "and", num2, "is", findGCD(num1, num2))

# Method 4: Modulo Recursive Euclidean Algorithm: Repeated Subtraction
# This method improves complexity of repeated subtraction
# By efficient use of modulo operator in euclidean algorithm
def getGCD(a, b):
    return b == 0 and a or getGCD(b, a % b)
num1 = 36
num2 = 60
print("GCD of", num1, "and", num2, "is", getGCD(num1, num2))

# Method 5: Handling Negative Numbers in GCD
# This method improves complexity of repeated subtraction
# By efficient use of modulo operator in Euclidean algorithm
def getGCD(a, b):
    return b == 0 and a or getGCD(b, a % b)
num1 = -36
num2 = 60
# if user enters negative number, we just changing it to positive
# By definition GCD is the highest positive number that divides both numbers
# -36 & 60 : GCD = 12 (as highest num that divides both)
# -36 & -60 : GCD = 12 (as highest num that divides both)
num1 >= 0 and num1 or -num1
num2 >= 0 and num2 or -num2
print("GCD of", num1, "and", num2, "is", getGCD(num1, num2))


# Binary to Decimal to conversion :
# Method 1:Algorithmic way (Binary to Decimal)
# Time Complexity – O(N), where N is the count of the digits in the binary number
# Space Complexity – O(1), Constant Space
num = 10
binary_val = num
decimal_val = 0
base = 1
while num > 0:
    rem = num % 10
    decimal_val = decimal_val + rem * base
    num = num // 10
    base = base * 2
print("Binary Number is {}\nDecimal Number is {}".format(binary_val, decimal_val))

# Method 2:Inbuilt Method (Binary to Decimal)



# Octal to Decimal conversion :
# Method 1:Algorithmic way (Octal to Decimal)
def OctalToDecimal(num):
    decimal_value = 0
    base = 1
    while num:
        last_digit = num % 10
        num = int(num / 10)
        decimal_value += last_digit * base
        base = base * 8
    return decimal_value
octal = 512
print("The decimal value of",octal, " is",OctalToDecimal(octal))

# Method 2: Inbuilt Method (Octal to Decimal)
octal_num = 512
decimal_value = int(str(octal_num), 8)
print("The decimal value of {} is {}".format(octal_num, decimal_value))


# Hexadecimal to Decimal conversion:
def convert(hex):
    l = len(hex)
    decimal = 0
    pos = 0
    for i in range(l - 1, -1, -1):
        # if given index value is a digit (0 - 9)
        if '0' <= hex[i] <= '9':
            # if hex[i] is in range '0' - '9'
            # can convert string value to its integer value
            # by passing it to int() function
            digit = int(hex[i])
            decimal += digit * pow(16, pos)
            pos += 1
        # if given index is char in range [A, F]
        elif 'A' <= hex[i] <= 'F':
            # if hex[i] is in range 'A' - 'F'
            # can convert sting value to its int value
            # by subtracting 55(Refer Ascii table) as
            # ASCII val A: 65 and A must result 10 as value
            # to get ASCII value in Python can use ord() function
            digit = ord(hex[i]) - 55
            decimal += digit * pow(16, pos)
            pos += 1
    return decimal
hex = "C9"
print("decimal value of", hex, "is", convert(hex))


# Decimal to Binary conversion:
# Method 1: Binary Bits stored in Array
def convertBinary(num):
    binaryArray = []
    while num>0:
        binaryArray.append(num%2)
        num = num//2
    for j in binaryArray:
        print(j, end="")
decimal_num = 21
convertBinary(decimal_num)

# Method 2: Using mathematical operations to generate binary equivalent.
def convertBinary(num):
    binary = 0
    i, rem = 1, 0
    while num != 0:
        rem = num % 2
        num = num // 2
        binary += rem * i
        i *= 10
    return binary
decimal_num = 21
print("Binary of", decimal_num, "is : ", end="")
print(convertBinary(decimal_num))


# Decimal to Octal Conversion:
# Algorithm  ( Method 1 )
decimal = 148
octal = []
while decimal > 0:
    r = decimal % 8
    octal.append(r)
    decimal = decimal // 8
for i in reversed(octal):
    print(i, end="")

# Algorithm  ( Method 2 )
decimal = 33
octal = 0
count = 1
while decimal > 0:
    r = decimal % 8
    octal += r * count
    count *= 10
    decimal = decimal // 8
print(octal)


# Decimal to Hexadecimal Conversion:
def convert(num):
    hexa = []
    while num != 0:
        rem = num % 16
        if rem < 10:
            hexa.append(chr(rem + 48))
        else:
            hexa.append(chr(rem + 55))
        num = num // 16
    hexa.reverse()
    return ''.join(hexa)
decimal = 2545
print("Hexadecimal :", convert(decimal))


# Binary to Octal conversion :
# Method 1:
# function to convert binary to octal
def convert(num):
    octalDigit = 0
    count = 1
    i = 0
    pos = 0
    octalArray = [0] * 32
    while num != 0:
        digit = num % 10
        octalDigit += digit * pow(2, i)
        i += 1
        num //= 10
        # placing current octal-sum for 3 pair in array index position
        octalArray[pos] = octalDigit
        # whenever we have read next 3 digits
        # setting values to default
        # increasing pos so next values can be placed at next array index
        if count % 3 == 0:
            octalDigit = 0
            i = 0
            pos += 1
        count += 1
    # printing octal array in reverse order
    for j in range(pos, -1, -1):
        print(octalArray[j], end='')
binary = 1010
convert(binary)

# Method 2:
# function to convert binary to octal
def convert(num):
    octalDigit = 0
    count = 1
    i = 0
    pos = 0
    octalArray = [0] * 32
    while num != 0:
        digit = num % 10
        octalDigit += digit * pow(2, i)
        i += 1
        num //= 10
        # placing current octal-sum for 3 pair in array index position
        octalArray[pos] = octalDigit
        # whenever we have read next 3 digits
        # setting values to default
        # increasing pos so next values can be placed at next array index
        if count % 3 == 0:
            octalDigit = 0
            i = 0
            pos += 1
        count += 1
    # printing octal array in reverse order
    for j in range(pos, -1, -1):
        print(octalArray[j], end='')
binary = 10101111
convert(binary)


# Octal to Binary conversion : 
#Method 1:
def convert(octal):
    i = 0
    decimal = 0
    while octal != 0:
        digit = octal % 10
        decimal += digit * pow(8, i)
        octal //= 10
        i += 1
    print("Decimal Value :", decimal)
    binary = 0
    rem = 0
    i = 1
    while decimal != 0:
        rem = decimal % 2
        decimal //= 2
        binary += rem * i
        i *= 10
    print("Binary Value :", binary)
octal = int(input("Octal Value : "))
convert(octal)

# Method 2
def convert(octal):
    print("Equivalent Binary Number: ", end="")
    for i in range(len(octal)):
        switcher = {
            0: "000",
            1: "001",
            2: "010",
            3: "011",
            4: "100",
            5: "101",
            6: "110",
            7: "111"
        }
        print(switcher.get(int(octal[i]), "Invalid Octal Number"), end="")
octal = list(input("Insert an octal number: "))
convert(octal)


# Quadrants in which a given coordinate lies :
# for initialization of coordinates
x, y = map(int, list(input("Insert the value for variable X and Y : ").split(" ")))
# find true condition of first quadrant
if x > 0 and y > 0:
    print("point (", x, ",", y, ") lies in the First quadrant")
# find second quadrant
elif x < 0 and y > 0:
    print("point (", x, ",", y, ") lies in the Second quadrant")
# To find third quadrant
elif x < 0 and y < 0: 
    print("point (", x, ",", y, ") lies in the Third quadrant")
 # To find Fourth quadrant 
elif x > 0 and y < 0:
    print("point (", x, ",", y, ") lies in the Fourth quadrant")
# To find does not lie on origin
elif x == 0 and y == 0:
    print("point (", x, ",", y, ") lies at the origin")
# On x-axis
elif y == 0 and x != 0:
    print("point (", x, ",", y, ") on x-axis")
# On y-axis
elif x == 0 and y != 0:
    print("point (", x, ",", y, ") on at y-axis")



# 
# 
# Codes for Recursion
# 
# 