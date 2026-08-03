class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        i = 0
        res = []
        for word in strs:
            if sorted(word) not in d:
                d[sorted(word)] = i
                i += 1
                res.append([word])
            else:
                res[d[sorted(word)]].append(word)
        return res
          
        