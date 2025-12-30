class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        br_dict = {
            '(':')',
            '[':']',
            '{':'}'
        }
        for br in s:
            if br in br_dict:
                stack.append(br)
            else:
                if not stack:
                    return False
                if br_dict[stack.pop()]!= br:
                     return False

        return not stack

        