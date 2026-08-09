import heapq

class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        
        intervals.sort(key=lambda x: x[0])
        
        
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        
        res = [-1] * len(queries)
        min_heap = []  
        i = 0
        n = len(intervals)
        
        for q, orig_idx in sorted_queries:
           
            while i < n and intervals[i][0] <= q:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(min_heap, (length, right))
                i += 1
                
            
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
                
            
            if min_heap:
                res[orig_idx] = min_heap[0][0]
                
        return res
        