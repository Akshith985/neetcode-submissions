import heapq
class MedianFinder:

    def __init__(self):
        # Max-Heap to store the smaller half of numbers (inverted to negative)
        self.small_heap = [] 
        # Min-Heap to store the larger half of numbers
        self.large_heap = [] 

    def addNum(self, num: int) -> None:
        # 1. Push to small_heap (Max-Heap) first
        heapq.heappush(self.small_heap, -num)
        
        # 2. Make sure every element in small_heap is <= every element in large_heap
        # We do this by passing the maximum of the small half over to the large half
        val = -heapq.heappop(self.small_heap)
        heapq.heappush(self.large_heap, val)
        
        # 3. Maintain the size property: len(small_heap) >= len(large_heap)
        if len(self.large_heap) > len(self.small_heap):
            val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -val)

    def findMedian(self) -> float:
        # If total number of elements is odd, small_heap has the exact median at its peak
        if len(self.small_heap) > len(self.large_heap):
            return float(-self.small_heap[0])
            
        # If total number of elements is even, calculate the average of both peaks
        return (-self.small_heap[0] + self.large_heap[0]) / 2.0
        
        