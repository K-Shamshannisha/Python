# using a loop
arr1=[1,2,3,4,5]
arr2=[5,6,7,8,9]
def find_matches(arr1,arr2):
    matches=[]
    for elem in arr1:
        if elem in arr2:
            matches.append(elem)
    return matches
print(find_matches(arr1,arr2))

# using list comprehension
def find_match(arr1,arr2):
    return [elem for elem in arr1 if elem in arr2]
arr1=[1,2,3,4,5]
arr2=[4,5,6,7,8,9]
print(find_match(arr1,arr2))

# using set intersection
def matches(arr1,arr2):
    return list(set(arr1) & set(arr2))
arr1=[1,2,3,4,5]
arr2=[4,5,6,7,8]
print(find_matches(arr1,arr2))



