class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict(int)
        queue = deque()

        for ch in s:
            freq[ch] += 1
            if ch not in queue:
                queue.append(ch)
        while queue and freq[queue[0]] > 1:
            queue.popleft()
        return s.find(queue[0]) if queue else -1