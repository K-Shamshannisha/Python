str="Hello World"

#dlroW olleH 

# slicing method
rev_str=str[::-1]
print(rev_str)

# reversed function
rev_str1="".join(reversed(str))
print(rev_str1)

# list comprehension
rev="".join([i for i in str][::-1] )
print(rev)

# reverse method
mylist=list(str)
mylist.reverse()
rev1="".join(mylist)
print(rev1)
