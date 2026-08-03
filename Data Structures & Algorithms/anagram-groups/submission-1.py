class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        i = 0
        res = []
        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word not in d:
                d[sorted_word] = i
                i += 1
                res.append([word])
            else:
                res[d[sorted_word]].append(word)
        return res
          
        