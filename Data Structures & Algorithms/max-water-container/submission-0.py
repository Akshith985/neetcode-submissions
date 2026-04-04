class Solution:
    def maxArea(self, heights: List[int]) -> int:
      left=0
      right=len(heights)-1
      max_v=0

      while left<right:
        width=right-left
        if heights[left]<heights[right]:
            h=heights[left]
            is_left_short=True
        else:
            h=heights[right]
            is_left_short=False
        current_v=width*h
        if current_v>max_v:
            max_v=current_v
        if is_left_short:
            left+=1
        else:
            right-=1
      return max_v

