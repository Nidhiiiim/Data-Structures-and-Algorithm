# LINEAR SEARCH ALGORITHM
## Used for small data sets
## Time Complexity O(n)
## Does not require sorting
## Used for non-linear Data Structures




class SearchArray:
    def __init__(self, array, key):
        self.array = array
        self.length = len(array)
        self.key = key

    def linear(self):
        for i in range(self.length):
            if self.array[i] == self.key:
                return i
        return -1  # Return -1 if key not found

    def binary(self):
        start = 0
        end = self.length - 1
        while start <= end:
            mid = (start + end) // 2
            if self.key == self.array[mid]:
                return mid
            elif self.key < self.array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1  # Return -1 if key not found

## INTERPOLATION SEARCH
# Good for uniformly distributed data
## Guess work


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 5

    search = SearchArray(array, key)

    if len(array) > 5:
        result = search.binary()
        print(f'Binary Search: Key {key} found at index: {result}')
    else:
        result = search.linear()
        print(f'Linear Search: Key {key} found at index: {result}')
