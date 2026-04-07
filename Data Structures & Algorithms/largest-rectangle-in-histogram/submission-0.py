class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l=[]
        heights.append(0)
        width=0
        max_area=0
        for i in range(len(heights)):
            while l and heights[i] < heights[l[-1]]:
                h = heights[l.pop()]
                if not l:
                    width = i
                else:
                    width = i - l[-1] - 1
                area = h * width
                max_area = max(max_area, area)
            l.append(i)
        return max_area

