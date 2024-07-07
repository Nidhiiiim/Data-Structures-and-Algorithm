######### TYPES OF ARRAYS ##########
# Static Array
import array

a = array.array('i', [2, 3, 2, 3, 5])
print("Static Array: ", a)

# Dynamic Array
b = []
b.append(1)
b.append(2)
b.append(3)
b.append(4)
print("Added Dynamically: ", b)

######### REVERSING ARRAY #############
# 1) Not in place
rev_a = a[::-1]
print("Not In place Reversed Array: ", rev_a)


# 2) Reverse In Place | 2 Pointer Approach
def inplacereverse(a):
    start = 0
    end = len(a) - 1
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
    print("In Place Reversed with 2 pointer, means no extra array space used: ", a)


# 3) Not In place | Inbuilt function

rev_b = reversed(b)
print("Reversed Array with inbuilt function: ", rev_b)


##### ARRAY SEARCHING ALGORITHMS ######
# 1. LINEAR SEARCH
def linearsearchalgo(c, k):
    for i in range(len(c)):
        if c[i] == k:
            print("Element Located at: ", i)
            return i
    return 0


# 2. BINARY SEARCH | RECURSIVELY
def binarysearchalgorecursive(c, low, high, b):
    # Must have sorted Array else first sort
    if high >= low:
        mid = low + (high - low) // 2
        if c[mid] == b:
            print(f"Element {b} Found using Binary Search with Recursion in ", c)
            return mid
        elif c[mid] > b:
            return binarysearchalgorecursive(c, low, mid-1, b)
        elif c[mid] < b:
            return binarysearchalgorecursive(c, mid + 1, high, b)
    else:
        print(f"Element {b} Not Found in Binary Search")
        return -1

# 3. BINARY SEARCH | LOOPS
def binarysearchloop(c, low, high, b):
    while high >= low:
        mid = low + (high - low) // 2
        if c[mid] == b:
            print(f"Element {b} Found using Binary Search with Loop in ", c)
            return mid
        elif c[mid] > b:
            high = mid - 1
        elif c[mid] < b:
            low = mid + 1
    print(f"Element {b} not Found in Binary Search")
    return -1


if __name__ == "__main__":
    c = [1, 3, 4, 56, 3, 5]
    s = [1, 2, 4, 45, 56, 60]
    k = 5
    b = 66
    # UNSORTED & LINEAR
    linearsearchalgo(c, k)
    inplacereverse(c)

    # SORTED & LINEAR | RECURSIVE
    binarysearchalgorecursive(s, 0, len(s)-1, b)

    # BINARY SEARCH WITH LOOPING
    binarysearchloop(s, 0, len(s) - 1, b)
