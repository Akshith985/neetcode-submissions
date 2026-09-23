class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
            
        N = n
        if N < 0:
            x = 1 / x
            N = -N
            
        res = 1.0
        current_product = x
        
        while N > 0:
            
            if N % 2 == 1:
                res *= current_product
                
          
            current_product *= current_product
            N //= 2
            
        return res