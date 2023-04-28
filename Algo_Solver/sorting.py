"""
These API's provides utilities for sorting arrays.

Functions:
 `bubble_sort`: Sorts array by swapping every adjacent pair.

 `insertion_sort`: Sorts array by swapping each element until it is in the right spot.

 `merge_sort`: Sorts array by reducing each array until it is 1 element then sorting individually.

 `quick_sort`: Sorts array by reducing each array by choosing a pivot and sorting accordingly.

 `radix_sort`: Sorts array based off the digits.
 
 `counting_sort`: Sorts array based off the pidgeonhole principle.

"""


def bubble_sort(arr):
    """
    This algorithm performs bubble sort on an array to sort it.

    Args:
        arr (array): The array we are given.

    Returns:
        array: The sorted version of the array.
    """
    array_len = len(arr)
    for i in range(array_len):
        for j in range(0, array_len - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    """
    Performs insertion sort on an array to sort it.

    Args:
        arr (array): The array we are given.

    Returns:
        array: The sorted version of the array.
    """
    array_len = len(arr)
    for i in range(1, array_len):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    """
    Performs merge sort on an array to sort it.

    Args:
        arr (array): The array we are given.

    Returns:
        array: The sorted version of the array.
    """
    array_len = len(arr)
    if array_len > 1:
        mid = array_len // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr):
    """
    Performs quick sort on an array to sort it.

    Args:
        arr (array): The array we are given.

    Returns:
        array: The sorted version of the array.
    """

    array_len = len(arr)
    if array_len <= 1:
        return arr
    pivot = arr[array_len // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def bucket_sort(arr):
    """
    Performs bucket sort on an array to sort it.

    Args:
        arr (array): The array we are given.

    Returns:
        array: The sorted version of the array.
    """

    max_val = max(arr)
    size = max_val / len(arr)

    buckets = [[] for _ in range(len(arr))]

    for i in range(len(arr)):
        j = int(arr[i] / size)
        if j != len(arr):
            buckets[j].append(arr[i])
        else:
            buckets[len(arr) - 1].append(arr[i])

    for i in range(len(arr)):
        insertion_sort(buckets[i])

    return [item for bucket in buckets for item in bucket]


def radix_sort(arr):
    """
    Performs radix sort on an array to sort it.

    Args:
        arr (array): The array we are given.

    Returns:
        array: The sorted version of the array.
    """

    max_val = max(arr)

    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr


def counting_sort(arr, exp):
    """
    Performs counting sort on an array to sort it.

    Args:
        arr (array): The array we are given.

    Returns:
        array: The sorted version of the array.
    """
    array_len = len(arr)
    output = [0] * array_len
    count = [0] * 10

    for i in range(array_len):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = array_len - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(array_len):
        arr[i] = output[i]


def two_pointer_sort(arr1, arr2):
    """
    Sorts two sorted arrays using a two-pointer algorithm.

    Args:
        arr1 (array): The first sorted array.
        arr2 (array): The second sorted array.

    Returns:
        array: A sorted array that merges the two input arrays.
    """
    sorted_arr = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    return sorted_arr


def heapify(arr, n, i):
    """
    A helper function to create a max heap.

    Args:
        arr (array): The input array.
        n (int): The size of the heap.
        i (int): The index to start heapifying from.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    """
    Sorts an input array using heapsort.

    Args:
        arr (array): The input array to sort.

    Returns:
        array: The sorted array.
    """
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr
