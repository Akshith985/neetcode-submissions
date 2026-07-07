class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        
        def calculate_and_sink_area(r, c):
            # BASE CASE: Out of bounds or hit water (0), contributes 0 area
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                grid[r][c] == 0):
                return 0
                
            # Sink the land cell so we don't count it again
            grid[r][c] = 0
            
            # Calculate total area: 1 (for current cell) + area of all 4 neighbors
            area = (1 + 
                    calculate_and_sink_area(r - 1, c) + # Up
                    calculate_and_sink_area(r + 1, c) + # Down
                    calculate_and_sink_area(r, c - 1) + # Left
                    calculate_and_sink_area(r, c + 1))  # Right
            
            return area

        # Scan the grid cell by cell
        for r in range(ROWS):
            for c in range(COLS):
                # If we hit land, measure the entire connected island mass
                if grid[r][c] == 1:
                    current_island_area = calculate_and_sink_area(r, c)
                    # Update our global record holder if this island is bigger
                    max_area = max(max_area, current_island_area)
                    
        return max_area 