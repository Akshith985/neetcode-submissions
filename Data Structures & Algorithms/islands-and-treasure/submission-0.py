from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify grid in-place instead.
        """
        if not grid:
            return
            
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        
        # 1. Gather all treasure chests ('0') to act as our multi-source starting layer
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    
        # 2. Run Layer-by-Layer BFS
        while queue:
            r, c = queue.popleft()
            
            # Look in all 4 cardinal directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                # Only step onto the cell if it's within bounds and is unvisited land (INF)
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647:
                    # The distance to the nearest chest is exactly 1 step further than current cell
                    grid[nr][nc] = grid[r][c] + 1
                    # Append neighbor to queue to continue expanding the ripple
                    queue.append((nr, nc))