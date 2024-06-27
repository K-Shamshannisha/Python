str1="silent"
str2="listen"

# sorting strings
def ane(str1,str2):
    return sorted(str1)==sorted(str2)
print(ane(str1,str2))

# using a dictionary to count character frequencies
def anagram(str1,str2):
    count1={}
    count2={}
    for char in str1:
        if char in count1:
            count1[char]+=1
        else:
            count2[char]=1
    for char in str2:
        if char in count2:
            count2[char]+=1
        else:
            count2[char]+1
    return count1==count2
print(anagram(str1,str2))

# using collections module
from collections import Counter
def aree(str1,str2):
    return Counter(str1)==Counter(str2)
print(aree(str1,str2))

# using a single loop
def anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    count ={}
    for char1,char2 in zip(str1,str2):
        if char1!=char2:
            if char1 in count:
                count[char1]+=1
            else:
                count[char1]=1
            if char2 in count:
                count[char2]-=1
            else:
                count[char2]=-1
    return all(val==0 for val in count.values())
print(anagram(str1,str2))