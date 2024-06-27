str="Hello World"
# using count method
def count_char_occurrences(s,char):
    return s.count(char)
print(count_char_occurrences(str,"o"))

# using a loop
def count_char(s,char):
    count=0
    for c in s:
        if c==char:
            count+=1
    return count
print(count_char(str,"l"))

# using a list comprehension
def count_chars(s,char):
    return len([c for c in s if c==char])
print(count_char(str,"l"))

# using sum function with generator 
def count(s,char):
    return sum (1 for c in s if c==char)
print(count(str,"o"))