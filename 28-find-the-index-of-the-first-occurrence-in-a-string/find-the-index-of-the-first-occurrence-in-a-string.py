class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #This is brute force approach - 0((n-m)*m) = 0(n*m)
        # word_len = len(needle)
        # for i in range(len(haystack) - word_len + 1):
        #     if haystack[i:i+word_len] == needle:
        #         return i
        # return -1

        #Use KMP algorithm - Time complexity : 0(n + m)
        LPS = [0]*len(needle)
        length = 0
        i = 1

        while i < len(needle):
            if needle[i] == needle[length]:
                length += 1
                LPS[i] = length
                i +=1
            else:
                if length != 0:
                    length = LPS[length - 1]
                else:
                    LPS[i] = 0
                    i +=1
        i = j = 0 # i for string and j for substring
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            
            if j == len(needle):
                return i - j

            elif i < len(haystack) and haystack[i] != needle[j]:
                if j != 0:
                    j = LPS[j - 1]
                else:
                    i += 1

        return -1 