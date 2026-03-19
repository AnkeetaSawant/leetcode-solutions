class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap_min = []
        self.k = k
        if len(nums)<= 0 :
            self.heap_min = [float('-inf')]  
        for num in nums:
            if len(self.heap_min) < self.k:
                heapq.heappush(self.heap_min, num)
            else:
                if num > self.heap_min[0]:
                    heapq.heapreplace(self.heap_min, num)


    def add(self, val: int) -> int:
        max_value = 0
        if len(self.heap_min) < self.k:
            heapq.heappush(self.heap_min,val)
        elif val > self.heap_min[0]:
            heapq.heapreplace(self.heap_min,val)

        return self.heap_min[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)