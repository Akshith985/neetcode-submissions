class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        m = len(matrix)
        L=0
        R=(m*n)-1
        while L<=R:
            mid=(L+R)//2
            val = matrix[mid // n][mid % n]
            if val==target:
                return True
            elif val>target:
                R=mid-1
            elif val<target:
                L=mid+1
        return False