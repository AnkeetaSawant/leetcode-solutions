class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        k_value = float('-inf')
        for i in range(len(nums)-1,-1, -1):
            if nums[i] < k_value:
                return True

            while stack and stack[-1] < nums[i]:
                k_value = stack.pop()

            stack.append(nums[i])

        return False
