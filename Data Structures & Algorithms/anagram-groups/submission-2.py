from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        kv = defaultdict(list)
        for word in strs:
            kv[tuple(sorted(word))].append(word)
        return list(kv.values())
            