from colorama import init
from termcolor import colored


"""

BinarySearch algorithm can only work with a sorted array. It finds the middle number. If the wanted number is
in the first half it repeats the algorithm only in the first half.
Same goes for the second half. It returns the index when it arrives on the desired number.

"""


# Method for the BinarySearch
def BinarySearch(arr, i, l, x):
    # Checks if the array isn't just one number

    if l >= i:
        # Finding the middle index in the array
        mid = i + (l - i) // 2

        # If the wanted number is the middle number, it returns the middle index
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            # If it's in the first half
            # Bug fix: Didn't know that i need to use return when calling a recursive function
            return BinarySearch(arr, i, mid - 1, x)
        else:
            # If it's in the second half
            return BinarySearch(arr, mid + 1, l, x)

    # If it's not found, it returns -1
    else:
        return -1


# Array and wanted number
array = [1, 2, 3, 4, 5]
x = int(input("Enter a number: "))

# Custom input for desired number
result = BinarySearch(array, 0, len(array) - 1, x)

if result != -1:
    print("The number is at the " + colored(str(result), 'green') + " index!")
else:
    print(colored('The number is not in the array!', 'red'))
