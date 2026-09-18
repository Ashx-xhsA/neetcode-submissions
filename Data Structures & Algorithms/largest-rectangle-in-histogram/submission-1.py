# the max area with the height of the ith bar, is with * height of ith bar. the width is (m - n) where n is the indice the closest left bar whose height is less than ith bar. n is the indice of the closest right bar whose height is less than ith bar
# so we iterate through each bar to find the max area of their height
# the trick is find m and n
# we use a non-decreasing stack
# append bar with indice to stack . if the top of the stack is bigger than current one, pop it and calculate it's max area
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        heights = [0] + heights + [0]
        stk = []
        for i in range(len(heights)):
            while stk and heights[stk[-1]] > heights[i]:
                height =  heights[stk.pop()]
                width = i - stk[-1] -1
                maxArea = max(maxArea, height * width)
            stk.append(i)
        return maxArea



        