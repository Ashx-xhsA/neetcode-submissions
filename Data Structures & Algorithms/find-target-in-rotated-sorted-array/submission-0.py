class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p = 0
        l,r = 0, len(nums) -1
        while l <r:
            m = l + (r-l)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        p = l
        n = len(nums)
        l,r = 0, n-1
        while l <= r:
            m = l + (r-l)//2
            if nums[(m+p)%n] == target:
                return (m+p)%n
            elif nums[(m+p)%n] > target:
                r = m -1 
            else:
                l = m + 1
        return -1
        