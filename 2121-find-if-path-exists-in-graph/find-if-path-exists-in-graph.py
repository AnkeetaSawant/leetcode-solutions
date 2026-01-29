class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        queue = deque([source])
        visited = set([source])
        graph_dict = defaultdict(list)
        for u,v in edges:
            graph_dict[u].append(v)
            graph_dict[v].append(u)
       
        while queue:
            
            node = queue.popleft()
            if node == destination:
                return True

            for neighbour in graph_dict[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return False
               
