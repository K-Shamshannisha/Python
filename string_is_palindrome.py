str="madam"

# Compare original string with its reverse
def is_palindromes(s):
    if s==s[::-1]:
        print("is a palindrome")
    else:
        print("not a palindrome")
res=is_palindromes(str)

# use a two-pointer approach
def palindrome(s):
    left,right=0,len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left +=1
        right -=1
    return True
print(palindrome(str))

# use a recursive function
def palindromes(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return palindromes(s[1:-1])
print(palindromes(str))


