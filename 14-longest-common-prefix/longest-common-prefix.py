class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        if not word:
            return ""
        
        for str in strs[1:len(strs)]:
            while not str.startswith(word):
                word = word[:-1]
                if not word:
                    return ""
                
        return word
        
