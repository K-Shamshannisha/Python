def find_second_largest(arr):
    if len(arr) < 2:
        return "No second largest element exists"
    max_num = second_max_num = float('-inf')
    for num in arr:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return "No second largest element exists"
    return second_max_num

# Example usage:
arr = [12, 35, 1, 10, 34, 1]
print(find_second_largest(arr))  # Output: 34