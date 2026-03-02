class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        for u, v in trust:
            graph[u].append(v)
            in_degree[v] += 1

        for person in range(1, n + 1):
            if len(graph[person]) == 0 and in_degree[person] == n -1:
                return person
        return -1


        
