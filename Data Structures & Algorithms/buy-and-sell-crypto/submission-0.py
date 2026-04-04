class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        profit=0
        for i in prices:
            if i<min_price:
                min_price=i
            else:
                p=i-min_price
                if p>profit:
                    profit=p
        return profit 