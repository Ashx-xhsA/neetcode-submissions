class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = r = 0
        used = 0
        while r <= len(s) -1:
            if used == 0:
                cur = s[r]
            if s[r] == cur:
                res = max(res,r-l+1)
                r+= 1
                continue
            if s[r] != cur and used < k:
                res = max(res,r-l+1)
                used += 1
                r += 1
                continue
            if s[r] != cur and used == k:
                while s[l] == cur:
                    l += 1
                r = l
                used = 0
        return res



        