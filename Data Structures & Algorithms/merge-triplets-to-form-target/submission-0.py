class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        tx, ty, tz = target
        good_indices = set()
        
        for a, b, c in triplets:
            
            if a > tx or b > ty or c > tz:
                continue
                
            
            if a == tx:
                good_indices.add(0)
            if b == ty:
                good_indices.add(1)
            if c == tz:
                good_indices.add(2)
                
            
            if len(good_indices) == 3:
                return True
                
        return len(good_indices) == 3