class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        min_diff = float('inf')

        if k == 1:
            return 0
        nums.sort()
        print(len(nums)-k+1)
        for i in range(len(nums)-k+1):
            print(i, nums[i + k - 1] - nums[i])
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])

        return min_diff
        