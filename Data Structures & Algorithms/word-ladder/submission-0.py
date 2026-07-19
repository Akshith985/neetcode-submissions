from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Quick exit: If the target word isn't even in the list, no sequence exists
        if endWord not in wordList:
            return 0
            
        # Ensure beginWord is part of the exploration space if not already present
        if beginWord not in wordList:
            wordList.append(beginWord)
            
        # 1. Build the wildcard adjacency pattern map
        # Example: {"h*t": ["hot", "hit"], "*ot": ["hot", "dot"]}
        pattern_map = defaultdict(list)
        word_len = len(beginWord)
        
        for word in wordList:
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)
                
        # 2. Set up BFS structures
        queue = deque([(beginWord, 1)]) # Stores tuples of (current_word, current_path_length)
        visited = {beginWord}
        
        # 3. Process BFS layer by layer
        while queue:
            word, length = queue.popleft()
            
            # Target reached! Return the total word count in the chain
            if word == endWord:
                return length
                
            # Generate all possible wildcard combinations for the current word
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i+1:]
                
                # Visit all neighboring words that match this structural pattern
                for neighbor in pattern_map[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, length + 1))
                        
                # Optimization: Clear the bucket once visited to reduce redundant lookups
                pattern_map[pattern] = []
                
        return 0