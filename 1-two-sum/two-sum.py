class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val not in hash_map:
                hash_map[nums[i]] = i
            else:
                return [hash_map[val], i]

        return 0      