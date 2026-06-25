class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)
            
            # Keep the heap size strictly at k
            # Evicts the smallest elements, leaving only the k largest
            if len(heap) > k:
                heapq.heappop(heap)
                
        # The top of the min-heap is the smallest of the k largest elements
        return heap[0]