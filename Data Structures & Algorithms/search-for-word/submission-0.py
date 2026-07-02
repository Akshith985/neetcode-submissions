class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, i):
            # BASE CASE 1: If our index matches the word length, we successfully found it!
            if i == len(word):
                return True
                
            # BASE CASE 2: Out of bounds, or current cell does not match the letter we need
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                board[r][c] != word[i]):
                return False
            
            # --- THE COMMIT STEP ---
            # Save the original character and mark the cell as visited using '#'
            temp = board[r][c]
            board[r][c] = "#"
            
            # Explore all 4 adjacent neighbors (Up, Down, Left, Right)
            # If ANY of these paths return True, then the search is a success!
            res = (dfs(r - 1, c, i + 1) or # Up
                   dfs(r + 1, c, i + 1) or # Down
                   dfs(r, c - 1, i + 1) or # Left
                   dfs(r, c + 1, i + 1))   # Right
            
            # --- THE BACKTRACK STEP ---
            # Restore the cell's original letter so other starting paths can use it
            board[r][c] = temp
            
            return res

        # Kickoff: Search from every single cell on the board
        for r in range(ROWS):
            for c in range(COLS):
                # If we find a path that successfully spells out the word, return True immediately
                if dfs(r, c, 0):
                    return True
                    
        return False