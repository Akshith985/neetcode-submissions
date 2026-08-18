class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        
        last_index = {char: i for i, char in enumerate(s)}
        
        partitions = []
        start = 0
        end = 0
        
        for i, char in enumerate(s):
            
            end = max(end, last_index[char])
            
        
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
                
        return partitions