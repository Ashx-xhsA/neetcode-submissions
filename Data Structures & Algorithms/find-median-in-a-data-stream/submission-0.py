import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        self.m = None
        

    def addNum(self, num: int) -> None:
        if not self.left and not self.right:
            heapq.heappush(self.right,num)
            self.m = num
            return
        if len(self.left) < len(self.right):
            heapq.heappush(self.left,-num)
        else:
            heapq.heappush(self.right,num)

        # make balance
        leftMax = -self.left[0]
        rightMin = self.right[0]
        if leftMax > rightMin:
            heapq.heappush(self.left,-heapq.heappop(self.right))
            heapq.heappush(self.right,-heapq.heappop(self.left))
        
        # set mid
        if len(self.left) !=len(self.right):
        
            self.m = self.right[0]
        else:
         
            self.m = (self.right[0]-self.left[0])/2

    def findMedian(self) -> float:
        return self.m
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()