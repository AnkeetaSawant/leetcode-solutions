class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea, left_pt, right_pt = 0, 0, len(height) - 1
        while left_pt <  right_pt:
            maxArea = max(maxArea, min(height[left_pt],height[right_pt])*(right_pt - left_pt) )
            if height[left_pt] <= height[right_pt]:
                left_pt = left_pt + 1
            else:
                right_pt = right_pt - 1

        return maxArea

