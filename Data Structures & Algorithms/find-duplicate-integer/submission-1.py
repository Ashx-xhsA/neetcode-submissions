class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # d = {}
        # for num in nums:
        #     d[num] = d.get(num,0) + 1
        # for key, val in d.items():
        #     if val != 1:
        #         return key

        li = [0] * (len(nums))
        for num in nums:
            if li[num] != 0:
                return num
            li[num] = 1
        