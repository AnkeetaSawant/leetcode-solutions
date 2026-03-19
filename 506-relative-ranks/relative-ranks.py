class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank_dict = {0:'Gold Medal',1:'Silver Medal',2:'Bronze Medal'}
        rank_heap = []
        for index,s in enumerate(score):
            heapq.heappush(rank_heap,(-s,index))
        output = [0]*len(score)
        counter = 0
        len_heap = len(rank_heap)
        while counter < len_heap:
            score,index = heapq.heappop(rank_heap)
            output[index] = rank_dict.get(counter, str(counter + 1))
            counter = counter + 1
        return output