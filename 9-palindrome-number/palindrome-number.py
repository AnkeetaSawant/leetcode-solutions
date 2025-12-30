class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False

        reversed_no = 0
        original_no = x

        while x > 0:
            reversed_no = reversed_no * 10 + (x % 10)
            x //= 10

        if reversed_no == original_no:
            return True
        return False