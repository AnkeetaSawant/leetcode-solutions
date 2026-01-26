class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_dict = {}
        for i in range(len(arr) - 1):
            diff = abs(arr[i + 1] - arr[i])
            if diff in min_dict:
                min_dict[diff] += [[arr[i],arr[i + 1]]]
            else:
                min_dict[diff] = [[arr[i],arr[i + 1]]]
        return min_dict[min(min_dict)]