class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        current = []
        res = []
        visited = set()
        def backtrack():
            if len(current) == len(nums):
                res.append(current.copy())
                return
            for num in nums:
                if num in visited:
                    continue
                current.append(num)
                visited.add(num)
                backtrack()
                current.pop()
                visited.remove(num)
        backtrack()
        return res