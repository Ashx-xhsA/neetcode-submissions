class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        mp1 = defaultdict(int)
        mp2 = defaultdict(int)
        n= len(s1)
        for ch in s1:
            mp1[ch] += 1
        l = r = 0
        while r < len(s2):
            mp2[s2[r]] += 1
            
            while  r-l + 1 > n:
                mp2[s2[l]] -= 1
                if mp2[s2[l]] == 0:
                    del mp2[s2[l]]
                l += 1
                
            
            if r-l+1 == n:
                if mp1 == mp2:
                    return True
            r += 1
        return False
            
            

        