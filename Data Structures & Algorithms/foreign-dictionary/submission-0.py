from collections import deque

class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
       
        adj = {char: set() for word in words for char in word}
        in_degree = {char: 0 for word in words for char in word}
        
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    c1, c2 = w1[j], w2[j]
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        in_degree[c2] += 1
                    break
                    
        
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        order = []
        
        while queue:
            char = queue.popleft()
            order.append(char)
            
            for neighbor in adj[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        
        if len(order) < len(in_degree):
            return ""
            
        return "".join(order)