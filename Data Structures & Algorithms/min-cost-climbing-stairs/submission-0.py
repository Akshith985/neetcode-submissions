class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = cost[0]
        two = cost[1]
        for i in range(2, len(cost)):
            current = cost[i] + min(one,two)
            one = two
            two = current
        return min(one,two)