class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1 for _ in range(n)]
        aft = [1 for _ in range(n)]
        res = [1 for _ in range(n)]
        prod = 1
        for i in range(n-1,-1,-1):
            prod = prod * nums[i]
            aft[i] = prod
        prod = 1
        for j in range(n):
            prod *= nums[j]
            pre[j] = prod
        res[0] = aft[1]
        res[-1] = pre[-2]
        for k in range(1,n-1):
            res[k] = pre[k-1] * aft[k+1]
        return res
        

        