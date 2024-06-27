# Python program to copy all elements of one array into another array
def copy_array(source_array):
    # Creating a new array by copying elements from source_array
    destination_array = source_array[:]
    return destination_array
# Get input from the user
user_input = input("Enter the elements of the array separated by spaces: ")
# Convert the input string into a list of integers
source_array = list(map(int, user_input.split()))
# Copy elements from source_array to destination_array
destination_array = copy_array(source_array)
# Print both the source and destination arrays
print("Source Array:", source_array)
print("Destination Array:", destination_array)

# Python program to find the frequency of each element in the array
def find_frequencies(arr):
    frequency_dict = {}
    for element in arr:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    return frequency_dict
# Get input from the user
user_input = input("Enter the elements of the array separated by spaces: ")
# Convert the input string into a list of integers
array = list(map(int, user_input.split()))
# Find the frequencies of each element
frequencies = find_frequencies(array)
# Print the frequencies
print("Element frequencies in the array:", frequencies)

# Python program to left rotate the elements of an array
def left_rotate_array(arr, n):
    # Perform n left rotations
    n = n % len(arr)  # To handle cases where n is greater than the length of the array
    rotated_array = arr[n:] + arr[:n]
    return rotated_array
# Get input from the user
user_input = input("Enter the elements of the array separated by spaces: ")
array = list(map(int, user_input.split()))
# Get the number of rotations from the user
num_rotations = int(input("Enter the number of left rotations: "))
# Perform the left rotation
rotated_array = left_rotate_array(array, num_rotations)
# Print the original and rotated arrays
print("Original Array:", array)
print("Rotated Array:", rotated_array)

# Python program to print the duplicate elements of an array
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for element in arr:
        if element in seen:
            duplicates.add(element)
        else:
            seen.add(element)
    return list(duplicates)
# Get input from the user
user_input = input("Enter the elements of the array separated by spaces: ")
array = list(map(int, user_input.split()))
# Find the duplicate elements
duplicates = find_duplicates(array)
# Print the duplicate elements
print("Duplicate elements in the array:", duplicates)

# Python program to print the elements of an array
def print_array(arr):
    for element in arr:
        print(element)
# Get input from the user
user_input = input("Enter the elements of the array separated by spaces: ")
# Convert the input string into a list of integers
array = list(map(int, user_input.split()))
# Print the elements of the array
print("Elements of the array:")
print_array(array)

# Python program to print the elements of an array in reverse order
def print_reverse_array(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i])
# Get input from the user
user_input = input("Enter the elements of the array separated by spaces: ")
# Convert the input string into a list of integers
array = list(map(int, user_input.split()))
# Print the elements of the array in reverse order
print("Elements of the array in reverse order:")
print_reverse_array(array)

# Python program to print the elements of an array present on even position
def print_elements_at_even_positions(arr):
    for i in range(0, len(arr), 2):
        print(arr[i])
# Get input from the user
user_input = input("Enter the elements of the array separated by spaces: ")
# Convert the input string into a list of integers
array = list(map(int, user_input.split()))
# Print the elements at even positions in the array
print("Elements at even positions in the array:")
print_elements_at_even_positions(array)

# Python program to print the elements of an array present on odd position
def print_elements_at_odd_positions(arr):
    for i in range(1, len(arr), 2):
        print(arr[i])
# Get input from the user
user_input = input("Enter the elements of the array separated by spaces: ")
# Convert the input string into a list of integers
array = list(map(int, user_input.split()))
# Print the elements at odd positions in the array
print("Elements at odd positions in the array:")
print_elements_at_odd_positions(array)

# Python program to print the largest element in an array
def find_largest_element(arr):
    if not arr:
        return None  # Return None for empty array
    max_element = arr[0]  # Initialize max_element with the first element
    for element in arr[1:]:  # Iterate from the second element to the end
        if element > max_element:
            max_element = element
    return max_element
# Get input from the user
user_input = input("Enter the elements of the array separated by spaces: ")
# Convert the input string into a list of integers
array = list(map(int, user_input.split()))
# Find the largest element in the array
largest_element = find_largest_element(array)
# Print the largest element
if largest_element is not None:
    print("The largest element in the array is:", largest_element)
else:
    print("Array is empty.")

# Python program to print the smallest element in an array
def find_smallest_element(arr):
    if not arr:
        return None  # return None for empty array
    # Initialize the smallest element with the first element of the array
    smallest = arr[0]
    # Iterate through the array to find the smallest element
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest
def main():
    # Taking input from the user for the array
    print("Enter the elements of the array separated by space:")
    elements = input().strip().split()
    # Convert the input elements from string to integer
    arr = list(map(int, elements))
    # Call the function to find the smallest element
    smallest_element = find_smallest_element(arr)
    if smallest_element is not None:
        print(f"The smallest element in the array is: {smallest_element}")
    else:
        print("Array is empty. No smallest element.")
if __name__ == "__main__":
    main()

# Python program to print the number of elements present in an array
def main():
    # Taking input from the user for the array
    print("Enter the elements of the array separated by space:")
    elements = input().strip().split()
    # Calculate the number of elements in the array
    num_elements = len(elements)
    print(f"The number of elements in the array is: {num_elements}")
if __name__ == "__main__":
    main()

# Python program to print the sum of all elements in an array
def main():
    # Taking input from the user for the array
    print("Enter the elements of the array separated by space:")
    elements = input().strip().split()
    # Convert the input elements from string to integer
    arr = list(map(int, elements))
    # Calculate the sum of elements in the array
    total_sum = sum(arr)
    print(f"The sum of all elements in the array is: {total_sum}")
if __name__ == "__main__":
    main()

# Python program to right rotate the elements of an array
def right_rotate_array(arr, k):
    # Calculate the effective rotation (k % len(arr)) to handle cases where k > len(arr)
    k = k % len(arr)
    
    # Rotate the array using slicing
    arr[:] = arr[-k:] + arr[:-k]

def main():
    # Taking input from the user for the array
    print("Enter the elements of the array separated by space:")
    elements = input().strip().split()
    # Convert the input elements from string to integer
    arr = list(map(int, elements))
    # Taking input from the user for number of rotations
    k = int(input("Enter the number of rotations: "))
    # Perform right rotation
    right_rotate_array(arr, k)
    # Print the rotated array
    print(f"The array after {k} right rotations is:")
    print(arr)
if __name__ == "__main__":
    main()

# Python program to sort the elements of an array in ascending order
def main():
    # Taking input from the user for the array
    print("Enter the elements of the array separated by space:")
    elements = input().strip().split()
    # Convert the input elements from string to integer
    arr = list(map(int, elements))
    # Sort the array in ascending order
    arr.sort()
    # Print the sorted array
    print("The array sorted in ascending order is:")
    print(arr)
if __name__ == "__main__":
    main()

# Python program to sort the elements of an array in descending order
def main():
    # Taking input from the user for the array
    print("Enter the elements of the array separated by space:")
    elements = input().strip().split()
    # Convert the input elements from string to integer
    arr = list(map(int, elements))
    # Sort the array in descending order
    arr.sort(reverse=True)
    # Print the sorted array
    print("The array sorted in descending order is:")
    print(arr)
if __name__ == "__main__":
    main()

