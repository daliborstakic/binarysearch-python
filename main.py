# Method for the BinarySearch

"""

BinarySearch algorithm can only work with a sorted array. It finds the middle number. If the wanted number is
in the first half it repeats the algorithm only in the first half.
Same goes for the second half. It returns the index when it arrives on the desired number.

"""


def BinarySearch(arr, x, i, l):
    # Checks if the array isn't just one number
    if l >= 1:
        # Finding the middle index in the array
        mid = i + (l-1) // 2

        # If the wanted number is the middle number, it returns the middle index
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            # If it's in the first half
            BinarySearch(arr, x, i, mid - 1)
        else:
            # If it's in the second half
            BinarySearch(arr, x, mid + 1, l)

    # If it's not found, it returns -1
    else:
        return -1


array = [1, 3, 4, 5, 7, 8, 9, 13, 16, 18, 19, 20, 24, 25, 30, 33]
