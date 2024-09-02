# Import necessary modules
from timeit import repeat  # Used to measure the execution time of small code snippets
from random import randint  # Used to generate random integers
from datetime import datetime  # Used to work with dates and times

import numpy as np  # Import numpy for numerical operations (not used in this code)

# Function to run the sorting algorithm and measure execution time
def run_sorting_algorithm(algorithm, array):
    # Prepare the setup code for importing the sorting function
    # Only import the function if it's not the built-in `sorted()`
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    # Create the statement to execute the algorithm on the array
    stmt = f"{algorithm}({array})"

    # Run the sorting algorithm 10 times and record the execution time
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Print the name of the algorithm and the minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")

# Bubble Sort function
def bubble_sort(arr):
    n = len(arr)  # Get the length of the array
    # Traverse through all array elements
    for i in range(n-1):
        # Last i elements are already sorted, so skip them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort function
def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        min_idx = i  # Assume the current index is the minimum
        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j  # Update min_idx if a smaller element is found
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Insertion Sort function
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Select the element to be placed at the correct position
        j = i-1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Place the key element in its correct position

# Merge Sort function
def merge_sort(arr):
    # If array has more than one element
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        L = arr[:mid]  # Divide the array into two halves
        R = arr[mid:]

        merge_sort(L)  # Sort the first half
        merge_sort(R)  # Sort the second half

        i = j = k = 0  # Initialize index variables for merging
        # Merge the two halves back together
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if any
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if any
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Partition function used in Quick Sort
def partition(start, end, array):
    pivot_index = start  # Set the starting point as the pivot
    pivot = array[pivot_index]  # Set the pivot value

    # Rearrange the array by comparing with the pivot
    while start < end:
        # Move the start pointer to the right until it finds an element greater than the pivot
        while start < len(array) and array[start] <= pivot:
            start += 1
        # Move the end pointer to the left until it finds an element smaller than the pivot
        while array[end] > pivot:
            end -= 1
        # Swap the elements if start is still less than end
        if start < end:
            array[start], array[end] = array[end], array[start]

    # Swap the pivot element with the element at the end pointer
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end  # Return the partition index

# Quick Sort function
def quick_sort(start, end, array):
    # Base case: if start is less than end, partition the array and sort the halves
    if start < end:
        p = partition(start, end, array)  # Get the partition index
        quick_sort(start, p - 1, array)  # Recursively sort the left half
        quick_sort(p + 1, end, array)  # Recursively sort the right half

# Define a minimum merge size for Tim Sort
MIN_MERGE = 32

# Calculate the minimum run size for Tim Sort
def calcMinRun(n):
    r = 0
    # Reduce n to below MIN_MERGE while keeping track of the least significant bit
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r  # Return the adjusted run size

# Insertion Sort function used in Tim Sort with custom left and right indices
def insertion_sort(arr, left, right):
    # Traverse from left+1 to right
    for i in range(left + 1, right + 1):
        j = i
        # Move the elements of arr that are greater than arr[j] one position ahead
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

# Merge function used in Tim Sort
def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m  # Calculate lengths of left and right subarrays
    left, right = [], []  # Create temporary arrays

    # Copy data to temporary arrays left[] and right[]
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l  # Initialize index variables for merging
    # Merge the left and right subarrays back into arr
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy the remaining elements of left[], if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    # Copy the remaining elements of right[], if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1



# Main section of the program
if __name__ == "__main__":
    ARRAY_LENGTH = 10000  # Define the length of the array
    # Generate an array of random integers between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    startTime = datetime.now()  # Record the start time
    print(startTime)  # Print the start time

    startTime = datetime.now()  # Reset the start time for sorting
    bubble_sort(array)  # Call the bubble sort function on the array

    end_time = datetime.now()  # Record the end time
    print(end_time - startTime)  # Print the time difference (execution time)
    
    print(end_time)  # Print the end time of the sorting process