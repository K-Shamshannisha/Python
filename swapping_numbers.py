# swapping 2 numbers without third variable

# using xor
a=5
b=10
a=a^b
b=a^b
a=a^b
print(a,b)

# using addition and subtraction
a=5
b=10
a=a+b
b=a-b
a=a-b
print(a,b)

# using tuple packing and unpacking
a=5
b=10
a,b=b,a
print(a,b)

# using a bitwise trick
a=5
b=40
a=(a&~b)|(b&~a)
b=(a&~b)|(b&~a)
a=(a&~b)|(b&~a)
print(a,b)