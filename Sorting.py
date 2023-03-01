# bubble sort
def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# insertion sort
def InsertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def MergeSort(arr):
    n = len(arr)
    if n > 1:
        # Divide the array into two halves
        mid = n // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively sort each half
        MergeSort(left_half)
        MergeSort(right_half)
        
        # Merge the two sorted halves
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

def QuickSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[n//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return QuickSort(left) + middle + QuickSort(right)

def BucketSort(arr):
    # Find the maximum element and calculate the bucket size
    max_val = max(arr)
    size = max_val/len(arr)

    # Create n empty buckets, where n is the length of the input array
    buckets = [[] for _ in range(len(arr))]

    # Put array elements in different buckets based on the bucket size
    for i in range(len(arr)):
        j = int(arr[i]/size)
        if j != len(arr):
            buckets[j].append(arr[i])
        else:
            buckets[len(arr) - 1].append(arr[i])

    # Sort the elements in each bucket using insertion sort
    for i in range(len(arr)):
        InsertionSort(buckets[i])

    # Concatenate the sorted buckets to get the sorted array
    return [item for bucket in buckets for item in bucket]


def RadixSort(arr):
    # Find the maximum number to know the number of digits
    max_val = max(arr)

    # Do counting sort for every digit
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Store count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr[] now
    # contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]

