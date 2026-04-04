class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        record=0
        l_max=0
        r_max=0
        v=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=l_max:
                    l_max=height[left]
                else:
                    v+=(l_max-height[left])
                left+=1
            else:
                if height[right]>=r_max:
                    r_max=height[right]
                else:
                    v+=(r_max-height[right])
                right-=1
        return v


       