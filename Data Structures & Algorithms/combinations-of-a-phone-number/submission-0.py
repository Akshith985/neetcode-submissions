class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        # 1. Define the phone keypad mapping
        digit_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        current = []
        
        def backtrack(i):
            # BASE CASE: If our index matches the length of the digits string,
            # we've generated a full complete word combination!
            if i == len(digits):
                res.append("".join(current))
                return
                
            # Get the current digit and its mapped pool of characters
            current_digit = digits[i]
            possible_letters = digit_map[current_digit]
            
            # Explore every character branch available for this specific digit
            for letter in possible_letters:
                # 1. Action: Commit to the letter
                current.append(letter)
                
                # 2. Recurse: Move to the next digit position (i + 1)
                backtrack(i + 1)
                
                # 3. Backtrack: Remove the letter to try the next one in the loop
                current.pop()

        # Kickoff the phone keypad string generator at index 0
        backtrack(0)
        return res