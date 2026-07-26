class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total_palindromes = 0

        def expand_around_center(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(n):
            total_palindromes += expand_around_center(i, i)
            
            
            total_palindromes += expand_around_center(i, i + 1)

        return total_palindromes