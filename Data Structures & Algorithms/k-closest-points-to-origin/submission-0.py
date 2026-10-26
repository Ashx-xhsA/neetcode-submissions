import math,heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        disInd = [(math.sqrt(point[0]**2 + point[1]**2),idx) for idx,point in enumerate(points)]
        res = []
        heapq.heapify(disInd)
        while len(res)<k:
            distance,pointIdx = heapq.heappop(disInd)
            res.append(points[pointIdx])
        return res