num=6
# iterative solution==>time complexity:O(n),auxiliary space:O(1)
def factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        while(n>1):
            fact*=n
            n-=1
        return fact
print("Factorial of",num,"is",factorial(num))

# recursive solution==>O(n),O(n)
def fact(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1)
print(fact(num))

# one-line solution(using ternary operator)==>O(n),O(n)
def facts(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1)
print(facts(num))

# Prime factorization method==>O(n),O(1)
def prime_fact(n):
    factors={}
    i=2
    while i*i<=n:
        while n%i==0:
            if i not in factors:
                factors[i]=1
            else:
                factors[i]+=1
            n//=i
        i+=1
    if n>1:
        if n not in factors:
            factors[n]=1
        else:
            factors[n]+=1
    return factors
def factorials_num(n):
    fact=1
    for p,k in prime_fact(n).items():
        fact *=p**k
    return fact
print(factorials_num(num))
