# BUBBLE SORT
def bubble(array):
    n = len(array)
    i = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


# Time Complexity O(n^2)
# Space Complexity O(1)

# SELECTION SORT ALGORITHM
# Every iteration a min value is assigned
# If element is bigger than min then it is replaced
def selection(array):
    n = len(array)

    # First loop for first pointer to left
    for i in range(n):
        # Initialise min_index to i for every iteration
        min_index = i
        # Second Pointer from next position to i
        for j in range(i + 1, n):
            # If element at j is smaller than element at i
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

# MERGE SORT


# QUICK SORT


# INSERTION SORT

arr = [1, 24, 4, 5, 6, 8]
print(bubble(arr))
print(selection(arr))
