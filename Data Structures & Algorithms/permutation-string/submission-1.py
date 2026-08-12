class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m= len(s1)
        n = len(s2)
        matches = 0
        if m > n:
            return False
        c1 = [0 for _ in range(26)]
        c2 = [0 for _ in range(26)]
        for i in range(m):
            c1[ord(s1[i])-ord('a')] += 1
            c2[ord(s2[i])-ord('a')] += 1
        for k in range(26):
            if c1[k] == c2[k]:
                matches += 1
        if matches == 26:
                return True
        l = 0
        r = m
        while r <= n-1:
            ir = ord(s2[r])-ord('a')
            c2[ir] += 1
            if c1[ir] == c2[ir]:
                matches += 1
            elif c2[ir]-1 == c1[ir]:
                matches -= 1
            
            il = ord(s2[l])-ord('a')
            c2[il] -= 1
            if c1[il] == c2[il]:
                matches += 1
            elif c2[il]+1 == c1[il]:
                matches -= 1
            
            if matches == 26:
                return True
            r+=1
            l += 1

        return False


