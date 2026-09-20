class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        if nums[0] <= nums[-1]:
            return nums[0]
        while l <r:
            mid = l + (r-l) //2
            if r == l + 1:
                return min(nums[r],nums[l])
            if nums[mid] > nums[r]:
                l = mid 
            elif nums[mid] <nums[l]:
                r = mid 

        
        