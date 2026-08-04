class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        kv = DefaultDict(int)
        for num in nums:
            kv[num] += 1
        b = [[] for _ in range(len(nums) + 1)]
        for key,value in kv.items():
            b[value].append(key)
        for i in range(len(nums),-1,-1):
            if len(res) == k:
                break
            if not b[i]:
                continue
            for v in b[i]:
                res.append(v)
        return res
