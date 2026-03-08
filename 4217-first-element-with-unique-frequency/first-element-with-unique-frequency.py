class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        freq_num = defaultdict(int)
        freqCount = defaultdict(int)
        for num in nums:
            freq_num[num] += 1
        for key,value in freq_num.items():
            freqCount[value] += 1
        
        for num in nums:
            if freqCount[freq_num[num]] == 1:
                return num
        return -1
        