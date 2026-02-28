class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's Algorithm - 0(n), this can also be done using divide & conquer method in 0(nlogn) time.
        max_sum = max_global = nums[0]
        start = end = temp_start = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i] + max_sum:
                max_sum = nums[i]
                temp_start = i
            else:
                max_sum = max(nums[i],nums[i] + max_sum)

            if max_sum > max_global:
                max_global = max_sum
                start = temp_start
                end = i

        return max_global