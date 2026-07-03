class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current = []
        
        # A simple helper function to check if a substring is a palindrome
        def is_palindrome(sub_str):
            return sub_str == sub_str[::-1]
            
        def backtrack(i):
            # BASE CASE: If our cutting index reaches the end of the string,
            # we have successfully partitioned the entire string into palindromes!
            if i >= len(s):
                res.append(current.copy())
                return
                
            # Loop through all possible next cutting positions
            for j in range(i, len(s)):
                # Take a tentative slice from index i to index j
                slice_chunk = s[i : j + 1]
                
                # Only proceed down this branch if the current slice is a palindrome
                if is_palindrome(slice_chunk):
                    # 1. Action: Add the valid palindrome slice to our current partition
                    current.append(slice_chunk)
                    
                    # 2. Recurse: Move our starting cut line forward past this chunk
                    backtrack(j + 1)
                    
                    # 3. Backtrack: Remove the chunk to try a wider/different slice point
                    current.pop()

        # Kickoff the slicing engine at index 0
        backtrack(0)
        return res