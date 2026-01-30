class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        '''len_edges = len(edges)
        graph_dict = defaultdict(list)
        visited_queue = deque([1])
        for u,v in edges:
            graph_dict[u].append(v)
            graph_dict[v].append(u)

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
        return 0'''
        #Above solution will scan all the nodes unnecessary increasing the  space and time complexity
        a,b = edges[0]
        x,y = edges[1]

        return a if a == y or a == x else b