class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        res=0
        while L<=R:
            mid=(L+R)//2
            hrs=0
            for p in piles:
                hrs+=(p + mid - 1) // mid
            if hrs<=h:
                res = mid
                R = mid - 1
            elif hrs>h:
                L = mid+1
        return res