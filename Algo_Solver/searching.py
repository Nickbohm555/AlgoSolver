"""Searching algorithms."""
import random


def binary_search(arr, num):
    """binary search algo."""
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
    """selection algo."""
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
