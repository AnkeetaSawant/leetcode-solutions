class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        queue = deque()
        visited = set()
        queue.append((0,0,[]))
        visited.add((0,0))

        while queue:
            A, B,path = queue.popleft()
            path = path + [(A,B)]

            if A == target or B == target:
                return True
            
            states = [
                (x,B), #fill jug A
                (A,y), #fill jug B
                (0,B), #empty A
                (A,0), #empty B               
            ]
            # Pour A -> B
            pour = min(A, y-B)
            states.append((x-pour,B+pour))

            #Pour B -> A
            pour = min(B, x-A)
            states.append((x+pour,y-pour))

            for state in states:
                if state not in visited:
                    visited.add(state)
                    queue.append((state[0],state[1],path))

        return False