import heapq


class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap (invert min-heap values to simulate max-heap)
        self.large = []  # Min-heap

    def addNum(self, num):
        # Add to max-heap (invert the value to simulate max-heap)
        heapq.heappush(self.small, -num)

        # Ensure every element in max-heap is less than or equal to every element in min-heap
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance the heaps if max-heap has more than one extra element compared to min-heap
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        # If max-heap has more elements, the median is its root
        if len(self.small) > len(self.large):
            return -self.small[0]
        # If heaps are equal, the median is the average of both roots
        return (-self.small[0] + self.large[0]) / 2


medianFinder = MedianFinder()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    medianFinder.addNum(number)
    print(f"Median after adding {number}: {medianFinder.findMedian()}")
