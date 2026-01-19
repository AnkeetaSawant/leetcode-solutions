class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea, left_pt, right_pt = float('-inf'), 0, len(height) - 1
        while left_pt <  right_pt:
            if height[left_pt] <= height[right_pt]:
                maxArea = max(maxArea, min(height[left_pt],height[right_pt])*(right_pt - left_pt) )
                left_pt = left_pt + 1
            else:
                maxArea = max(maxArea, min(height[left_pt],height[right_pt])*(right_pt - left_pt) )
                right_pt = right_pt - 1

        return maxArea

