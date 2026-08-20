from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        
        min_heap = [(0, k)] 
        shortest_times = {}
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            
            if node in shortest_times:
                continue
                
            shortest_times[node] = time
            
            
            if len(shortest_times) == n:
                return time
                
            for neighbor, weight in graph[node]:
                if neighbor not in shortest_times:
                    heapq.heappush(min_heap, (time + weight, neighbor))
                    
        
        return max(shortest_times.values()) if len(shortest_times) == n else -1