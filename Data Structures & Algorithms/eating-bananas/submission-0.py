import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            t = 0
            midk = l + (r-l)//2
            for p in piles:
                t += math.ceil(p/midk)
            
            if t > h:
                l = midk + 1
            elif t <= h:
                r = midk -1
        return l


