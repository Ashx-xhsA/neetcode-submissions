class Solution:
    def isValid(self, CountS,CountT):
        for k,v in CountT.items():
            if k not in CountS:
                return False
            elif CountS[k] < v:
                return False
        return True
                
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        res = [-float('inf'),float('inf')]
        CountS = defaultdict(int)
        CountT = defaultdict(int)
        for i in range(len(t)):
            CountT[t[i]] += 1
            CountS[s[i]] += 1
        if self.isValid(CountS,CountT):
            res = [0,len(t) -1]
        l=0 
        r = len(t) -1
        while r <= len(s)-1:
            while not self.isValid(CountS,CountT):
                r += 1
                if r == len(s):
                    break
                CountS[s[r]] += 1
            while l <= r and self.isValid(CountS,CountT):
                CountS[s[l]] -= 1
                l += 1
            if r < len(s) and r-(l-1) < res[1]-res[0]:
                res = [l-1,r]
        if res == [-float('inf'),float('inf')] :
            return ''
        else:
            return s[res[0]:res[1]+1]
        

            

            

        
        
        