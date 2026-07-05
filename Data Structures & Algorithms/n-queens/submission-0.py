class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        
        # Initialize an empty n x n board configuration using strings
        board = [["."] * n for _ in range(n)]
        
        # Tracking sets for fast O(1) safety verification
        cols = set()
        pos_diag = set() # Stores (r + c) constants
        neg_diag = set() # Stores (r - c) constants
        
        def backtrack(r):
            # BASE CASE: If we've successfully placed a queen in row n-1, 
            # we filled the board safely! Convert the array configuration to strings.
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
                
            # Try placing a queen in every column 'c' for the current row 'r'
            for c in range(n):
                # Check if the column or either diagonal is under attack
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue # Under fire! Skip this square.
                    
                # 1. Action: Commit to placing the Queen
                board[r][c] = "Q"
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                
                # 2. Recurse: Move to the next row down
                backtrack(r + 1)
                
                # 3. Backtrack: Undo placement and clean up tracking lines
                board[r][c] = "."
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                
        # Start the placement engine at Row 0
        backtrack(0)
        return res