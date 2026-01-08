class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        DP = [[float('-inf')]* (m) for _ in range(n)]
    
        for i in range(n):
            for j in range(m):
                prod = nums1[i] * nums2[j] 
                DP[i][j] = prod 
                if i > 0 and j > 0:
                    DP[i][j] = max(DP[i][j], prod + DP[i-1][j-1])
                
                if i > 0:
                    DP[i][j] = max(DP[i][j], DP[i-1][j])

                if j > 0:
                    DP[i][j] = max(DP[i][j], DP[i][j-1])
                
        return DP[n-1][m-1]

            
        