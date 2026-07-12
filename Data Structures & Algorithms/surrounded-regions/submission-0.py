from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
            
        ROWS, COLS = len(board), len(board[0])
        
        def rescue_dfs(r, c):
            # BASE CASE: Stop if out of bounds or if the cell is not an 'O'
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                board[r][c] != 'O'):
                return
                
            # Mark this cell as rescued by transforming it to 'T'
            board[r][c] = 'T'
            
            # Radiate out to all 4 neighbors to rescue the rest of the group
            rescue_dfs(r + 1, c) # Down
            rescue_dfs(r - 1, c) # Up
            rescue_dfs(r, c + 1) # Right
            rescue_dfs(r, c - 1) # Left

        # Step 1: Sweep the outer vertical borders (Left and Right columns)
        for r in range(ROWS):
            rescue_dfs(r, 0)        # Left border
            rescue_dfs(r, COLS - 1) # Right border
            
        # Step 2: Sweep the outer horizontal borders (Top and Bottom rows)
        for c in range(COLS):
            rescue_dfs(0, c)        # Top border
            rescue_dfs(ROWS - 1, c) # Bottom border

        # Step 3: Run the final transformation over the entire board
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    # Trapped! Captured by 'X's
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    # Safe! Restore its original form
                    board[r][c] = 'O'