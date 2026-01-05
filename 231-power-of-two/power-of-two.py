import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        if n <= 0:
            return False
        x = math.log2(n)
        return True if 2 ** int(x) == n else False'''

        return True if n > 0 and (n & (n - 1)) == 0 else False
            
                