
#
#SORTED = [2, 3, 5, 6, 8, 9, 10]
numbers = [5, 10, 9, 8, 6, 3, 2]
numbers_2 = [5, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9, 0]
print(numbers)
print('\n')


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_i = i
        for j in range(i, len(arr)):
            if arr[min_i] > arr[j]:
                min_i = j

        # temp = arr[i]
        # arr[i] = arr[min_i]
        # arr[min_i] = temp
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


def mergeSort(arr):
    def _merge(left, right):
        sorted_array = []

        while left and right:
            if left[0] > right[0]:
                sorted_array.append(right.pop(0))
            else:
                sorted_array.append(left.pop(0))
        while left:
            sorted_array.append(left.pop(0))
        while right:
            sorted_array.append(right.pop(0))

        return sorted_array

    n = len(arr)

    if n == 1:
        return arr

    arrOne = arr[0:n // 2]
    arrTwo = arr[n // 2:n]
    arrOne = mergeSort(arrOne)
    arrTwo = mergeSort(arrTwo)

    return _merge(arrOne, arrTwo)


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()  # chossing last item as pivot

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:  # greater than pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


# An optimized version of Bubble Sort
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already
        #  in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if not swapped:
            break


def binarySearchIteration(arr, target):
    if len(arr) == 1:
        return 0

    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


def binarySearchRecursive(arr, target, low, high):
    if low <= high:

        mid = (high + low) // 2

        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            return binarySearchRecursive(arr, target, mid + 1, high)
        else:
            return binarySearchRecursive(arr, target, low, mid - 1)

    return -1


sorted_numbers = [10, 20, 30, 40, 60, 110, 120, 130, 170]

a = binarySearchRecursive(sorted_numbers, 40, 0, len(sorted_numbers) - 1)
print(sorted_numbers[a])

a = binarySearchIteration(sorted_numbers, 40)
print(sorted_numbers[a])
