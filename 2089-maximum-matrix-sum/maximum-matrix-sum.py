class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        max_sum = 0
        negative_count = 0
        min_abs = float('inf')
        print(min_abs)
        for row in matrix:
            for col in row:
                if col < 0:
                    negative_count = negative_count + 1
                
                abs_col = abs(col)
                max_sum = max_sum + abs_col
                min_abs = min(min_abs, abs_col)
                

        if negative_count % 2 == 1:
            max_sum -= 2 * min_abs

        return max_sum
        