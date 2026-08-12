class Solution:
    def findMostFrequent(self,mp):
        res = ''
        mf = 0
        for key, val in mp.items():
            if val > mf:
                res = key
                mf = val
        return res

    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = r = 0
        mp = defaultdict(int)
        while r <= len(s)-1:
            c = s[r]
            mp[c] += 1

            mf = self.findMostFrequent(mp)
            while r-l+1 - mp[mf] > k:
                mp[l] -= 1
                l += 1
                mf = self.findMostFrequent(mp)
            
            res = max(res,r-l+1)
            r += 1
        return res
        