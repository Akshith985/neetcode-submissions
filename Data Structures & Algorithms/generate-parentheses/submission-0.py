class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        current = []
        
        def backtrack(open_count, close_count):
            # BASE CASE: If we have used exactly n opening and n closing parentheses,
            # the string is complete and perfectly well-formed!
            if open_count == close_count == n:
                res.append("".join(current))
                return
            
            # CHOICE 1: Add an opening parenthesis '('
            # We can always add an open bracket if we haven't hit our limit of n
            if open_count < n:
                current.append('(')
                backtrack(open_count + 1, close_count)
                current.pop() # Backtrack clean up
                
            # CHOICE 2: Add a closing parenthesis ')'
            # We can only add a close bracket if it matches an active, open bracket
            if close_count < open_count:
                current.append(')')
                backtrack(open_count, close_count + 1)
                current.pop() # Backtrack clean up
                
        # Start with 0 open and 0 close brackets used
        backtrack(0, 0)
        return res