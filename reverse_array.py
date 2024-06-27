# using a temporary variable
arr=[8,9,2,4,1]
def rev_arry(arr):
    reversed_arr=[]
    for i in range(len(arr)-1,-1,-1):
        reversed_arr.append(arr[i])
    return reversed_arr
print(rev_arry(arr))

# using slicing
def reverse(arr):
    return arr[::-1]
print(reverse(arr))

# using reversed function
def reve_array(arr):
    return list(reversed(arr))
print(reve_array(arr))

# in-phase reversal
def array_rev(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
print(array_rev(arr))