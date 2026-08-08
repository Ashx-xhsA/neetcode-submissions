class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1 or len(height) == 2:
            return 0

        left = [0 for _ in range(len(height))]
        right = [0 for _ in range(len(height))]
        left[0] = height[0]
        right[-1] = height[-1]
        for i in range(1,len(height)):
            left[i] = max(left[i-1],height[i])
        for j in range(len(height)-2,-1,-1):
            right[j] = max(right[j+1],height[j])
        res = 0
        for k in range(1,len(height)-1):
            cur = min(left[k-1],right[k+1]) - height[k]
            if cur > 0:
                res += cur
        return res


