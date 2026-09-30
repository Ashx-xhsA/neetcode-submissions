class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num,0) + 1
        for key, val in d.items():
            if val != 1:
                return key
        