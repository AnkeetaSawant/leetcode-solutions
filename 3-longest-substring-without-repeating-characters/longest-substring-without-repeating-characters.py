class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start , end = 0 , 0
        n = len(s)
        visitedDict = {}
        
        while end < n:
            if s[end] in visitedDict and visitedDict[s[end]] >= start:
                start = visitedDict[s[end]] + 1
            
            visitedDict[s[end]] = end
            max_len = max(max_len, end - start + 1)
            end = end + 1
        return max_len