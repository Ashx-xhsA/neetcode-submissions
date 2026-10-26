import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-stone for stone in stones]
        heapq.heapify(h)
        while len(h) > 1:
            x = heapq.heappop(h)
            y = heapq.heappop(h)
            if x == y:
                continue
            heapq.heappush(h,x-y if x-y <0 else y-x)
        return -h[0] if len(h)>0 else 0
        