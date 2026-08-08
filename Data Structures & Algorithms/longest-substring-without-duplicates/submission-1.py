class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 0
        l=r= 0
        sset = set()
        while r <= len(s)-1:
            if s[r] not in sset:
                sset.add(s[r])
                res = max(res, r-l+1)
                r += 1
            else:
                while s[l] != s[r]:
                    sset.remove(s[l])
                    l += 1
                sset.remove(s[l])
                l += 1
                
            
        return res


            
            


        