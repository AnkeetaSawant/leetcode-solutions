class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        len_edges = len(edges)
        graph_dict = defaultdict(list)
        visited_queue = deque([1])
        distinct_node = set()
        for u,v in edges:
            graph_dict[u].append(v)
            graph_dict[v].append(u)
        print(graph_dict)
        while visited_queue:
            node = visited_queue.popleft()
            counter = 0
            for neighbour in graph_dict[node]:
                counter = counter + 1
                if counter >= len_edges:
                    return node
                else:
                    counter = counter + 1
                    visited_queue.append(neighbour)
        return 0