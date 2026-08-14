class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = [0]
        res = [0 for _ in range(len(temperatures))]
        for i in range(1,len(temperatures)):
            cur = temperatures[i]
            while stk and cur > temperatures[stk[-1]]:
                res[stk[-1]] = i - stk[-1]
                stk.pop()
            stk.append(i)
        return res
        