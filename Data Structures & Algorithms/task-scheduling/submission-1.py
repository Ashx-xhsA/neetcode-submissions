from collections import deque
import heapq

# a a a a a bbbb vvvvv 2

# map a->10 v->5
# h = heapify[4] 
# q= [(4,2+2),(3,3+2)]
# time -> CPU time + 1 + 1 + 1
# * * * 




class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        h = [-value for value in count.values()]
        heapq.heapify(h)
        q = deque()
        time = 0
        while q or h:
            time += 1

            if q:
                if q[0][1] == time:
                    heapq.heappush(h,-q.popleft()[0])

            if h:
                c = -heapq.heappop(h)
                if c - 1:
                    q.append([c-1,time + n + 1])
        return time



# X X Y Y
# X Y _ X Y 5

# a a a b c
# bbb ac

# a c b __b __ b 9
# b _ _ b a c b 7

