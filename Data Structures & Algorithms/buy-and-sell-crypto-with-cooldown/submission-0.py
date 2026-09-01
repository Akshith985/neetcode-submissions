class Solution:
        def maxProfit(self, prices: list[int]) -> int:
                if not prices:
                        return 0
                held = -prices[0]
                sold = 0
                cooldown = 0
                for price in prices[1:]:
                        prev_sold = sold
                        sold = held + price
                        held = max(held, cooldown - price)
                        cooldown = max(cooldown, prev_sold)
                return max(sold, cooldown)