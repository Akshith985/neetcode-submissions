from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        minutes = 0
        
        # 1. Initialize the starting state
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c)) # Gather the multi-source rot nodes
                elif grid[r][c] == 1:
                    fresh_count += 1    # Track initial fresh fruit inventory
                    
        # If there are no fresh fruits to begin with, 0 minutes are needed
        if fresh_count == 0:
            return 0
            
        # 2. Process Layer-by-Layer BFS
        while queue and fresh_count > 0:
            minutes += 1
            # Process ALL rotten fruits currently in the queue for this specific minute block
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                # Check all 4 neighboring cells
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    
                    # If neighbor is within bounds and contains a FRESH fruit
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2       # Infect it!
                        fresh_count -= 1       # Reduce our inventory tracking
                        queue.append((nr, nc)) # It will spread rot next minute
                        
        # 3. Final Inspection Checkpoint
        return minutes if fresh_count == 0 else -1