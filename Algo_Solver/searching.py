"""
These API's provides utilities for searching algorithms.

Functions:
 `binary_search`: Performs binary search on an array to find the index of the number.
 `selection_algo`: Performs the selection sort algorithm to find the number associated with the index.

"""
import random


def binary_search(arr, num):
    """
    Performs binary search on an array given a specifc integer to find.

    Args:
        arr (array): The array we are searching.
        num (int): The integer we are looking for.

    Returns:
        int: The index of the specified number.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < num:
            low = mid + 1
        elif arr[mid] > num:
            high = mid - 1
        else:
            return mid
    return -1


def selection_algo(arr, k):
    """
    Performs selection algorithm on an array to find kth smallest value.

    Args:
        arr (array): An unsorted array.
        k (int): The index in the array from the end.

    Returns:
        int: The number of the kth smallest.
    """
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]
    if k < len(lows):
        return selection_algo(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return selection_algo(highs, k - len(lows) - len(pivots))


def linear_search(arr, num):
    """
    Performs linear search on an array given a specific integer to find.

    Args:
        arr (array): The array we are searching.
        num (int): The integer we are looking for.

    Returns:
        int: The index of the specified number.
    """
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1


def find_duplicates(arr):
    """
    Finds duplicates in an array using hashing.

    Args:
        arr (list): The array we are searching for duplicates.

    Returns:
        list: A list of all the duplicate elements in the array.
    """
    seen = set()
    duplicates = set()

    for elem in arr:
        if elem in seen:
            duplicates.add(elem)
        else:
            seen.add(elem)

    return list(duplicates)


def is_palindrome(s):
    """
    Checks if a given string is a palindrome or not.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())
    return s == s[::-1]


def count_values(head):
    """
    Counts the number of times each value appears in a linked list.

    Args:
        head (ListNode): The head node of the linked list.

    Returns:
        dict: A dictionary with keys as values in the linked list and values as the count of occurrences.
    """
    counts = {}
    curr = head
    while curr:
        if curr.val not in counts:
            counts[curr.val] = 1
        else:
            counts[curr.val] += 1
        curr = curr.next
    return counts
