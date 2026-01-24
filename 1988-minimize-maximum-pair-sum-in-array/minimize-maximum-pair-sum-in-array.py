class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        #This is the greedy algorithm problem, solved using sorting and left-right pointer.
        nums.sort()
        left, right, max_val = 0, len(nums) - 1 , float('-inf')
        while left < right:
            max_val = max(max_val, nums[left] + nums[right])
            left = left + 1
            right = right - 1

        return max_val