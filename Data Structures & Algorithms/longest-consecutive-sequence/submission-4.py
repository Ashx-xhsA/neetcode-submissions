class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashset = set()
        res = 1
        kv = {}
        for num in nums:
            hashset.add(num)
        for num in nums:
            count = 1
            nxt = num + 1
            while nxt in hashset:
                if nxt in kv:
                    count += kv[nxt]
                    break
                count += 1
                hashset.remove(nxt)
                nxt += 1
            kv[num] = count
            res = max(res,count)
        return res
            




        