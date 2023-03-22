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
