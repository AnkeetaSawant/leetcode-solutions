class Solution:
    def reverse(self, x: int) -> int:
        temp = 0
        negation = False
        if x < 0:
            x = abs(x)
            negation = True

        for i in range(len(str(abs(x))) - 1,-1, -1):
            temp += (x % 10) * (10 ** i)
            x = x // 10
             
        if (-2) ** 31 < temp < 2 ** 31 :
            return temp if not negation else -temp
        else:
            return 0