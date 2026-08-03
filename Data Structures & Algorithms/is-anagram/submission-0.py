class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        memo = {}
        for ch in s:
            if ch not in memo:
                memo[ch] = 0
            memo[ch] += 1
        for c in t:
            if c not in memo:
                return False
            memo[c] -= 1
        for v in memo.values():
            if v != 0:
                return False
        return True
        