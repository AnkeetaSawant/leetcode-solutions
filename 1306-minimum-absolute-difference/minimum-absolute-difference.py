class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_val = float('inf')
        res = []
        '''min_dict = {}
        for i in range(len(arr) - 1):
            diff = abs(arr[i + 1] - arr[i])
            if diff in min_dict:
                min_dict[diff] += [[arr[i],arr[i + 1]]]
            else:
                min_dict[diff] = [[arr[i],arr[i + 1]]]
        return min_dict[min(min_dict)]'''
        for i in range(len(arr) - 1):
            diff = abs(arr[i + 1] - arr[i])
            if diff < min_val:
                min_val = diff
                res = [[arr[i], arr[i + 1]]]
            elif diff == min_val :
                res += [[arr[i], arr[i + 1]]]
        return res
