from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(k):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
        res.append(q[0])
        for j in range(k,len(nums)):
            if nums[j-k] == q[0]:
                q.popleft()
            while q and q[-1] < nums[j]:
                q.pop()
            q.append(nums[j])
            res.append(q[0])
        return res
            
            
        

        

