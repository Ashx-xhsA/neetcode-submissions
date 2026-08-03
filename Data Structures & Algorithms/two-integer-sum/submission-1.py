class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        kv = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in kv:
                kv[num] = []
            kv[num].append(i)
        for j in range(len(nums)):
            num = nums[j]
            need = target - num
            if need == num:
                if len(kv[need])==1:
                    continue
                return [j,kv[need][1]]
            else:
                if need in kv:
                    return [j,kv[need][0]]
        