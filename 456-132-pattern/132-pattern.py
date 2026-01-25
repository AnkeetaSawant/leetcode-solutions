class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        kVal = float('-inf')
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < kVal:
                return True

            while stack and stack[-1]<nums[i]:
                kVal = stack.pop()
            stack.append(nums[i])

        return False
