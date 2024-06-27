# fibonacci series using recursion
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
def print_fibo(n):
    for i in range(n):
        print(fibo(i))
print(print_fibo(12))