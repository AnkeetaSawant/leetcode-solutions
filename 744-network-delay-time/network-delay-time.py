class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = {node: float('inf') for node in range(1,n+1)}
        print(dist)
        min_heap = [(0,k)]
        dist[k] = 0
        graph_dict = defaultdict(list)

        for u,v, w in times:
            graph_dict[u].append((v,w))

        while min_heap:
            current_weight, node = heapq.heappop(min_heap)

            if current_weight > dist[node]:
                continue
            
            for v,w in graph_dict[node]:
                new_dist = current_weight + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(min_heap,(new_dist,v))
        max_dist = max(dist.values())
        return max_dist if max_dist != float('inf') else -1