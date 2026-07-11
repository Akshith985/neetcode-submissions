from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
            
        ROWS, COLS = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()
        
        def dfs(r, c, visited, previous_height):
            # BASE CASES: 
            # 1. Out of bounds
            # 2. Cell already visited in this ocean's flood phase
            # 3. Water can't flow backward/upward here (current height is LOWER than previous)
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                (r, c) in visited or 
                heights[r][c] < previous_height):
                return
                
            # Mark this cell as reachable by the current ocean
            visited.add((r, c))
            
            # Radiate the flood upward/level to all 4 neighbors
            dfs(r + 1, c, visited, heights[r][c]) # Down
            dfs(r - 1, c, visited, heights[r][c]) # Up
            dfs(r, c + 1, visited, heights[r][c]) # Right
            dfs(r, c - 1, visited, heights[r][c]) # Left

        # 1. Kickoff floods from the horizontal borders (Top and Bottom rows)
        for c in range(COLS):
            # Top row borders the Pacific Ocean
            dfs(0, c, pacific_visited, heights[0][c])
            # Bottom row borders the Atlantic Ocean
            dfs(ROWS - 1, c, atlantic_visited, heights[ROWS - 1][c])
            
        # 2. Kickoff floods from the vertical borders (Left and Right columns)
        for r in range(ROWS):
            # Left column borders the Pacific Ocean
            dfs(r, 0, pacific_visited, heights[r][0])
            # Right column borders the Atlantic Ocean
            dfs(r, COLS - 1, atlantic_visited, heights[r][COLS - 1])
            
        # 3. Collect the intersections where a cell exists in both sets
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    res.append([r, c])
                    
        return res    