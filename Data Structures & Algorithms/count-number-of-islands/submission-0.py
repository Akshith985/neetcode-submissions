class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        ROWS, COLS = len(grid), len(grid[0])
        island_count = 0
        
        def sink_island(r, c):
            # Base Cases: Stop if we wander out of bounds or hit water ('0')
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                grid[r][c] == '0'):
                return
                
            # Sink the current land cell to prevent recounting it
            grid[r][c] = '0'
            
            # Recursively explore all 4 adjacent directions
            sink_island(r - 1, c) # Up
            sink_island(r + 1, c) # Down
            sink_island(r, c - 1) # Left
            sink_island(r, c + 1) # Right

        # Scan the entire grid cell by cell
        for r in range(ROWS):
            for c in range(COLS):
                # If we encounter land, it's a new island!
                if grid[r][c] == '1':
                    island_count += 1
                    # Trigger DFS to sink the entire connected landmass
                    sink_island(r, c)
                    
        return island_count