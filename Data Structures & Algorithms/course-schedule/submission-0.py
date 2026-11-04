from collections import deque,defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        shouldTakeBefore = defaultdict(int)
        mightTakeFromHere = defaultdict(list)
        # the number of courses that should be taken before taking a
        for a, b in prerequisites:
            shouldTakeBefore[a]= shouldTakeBefore[a] + 1
            mightTakeFromHere[b].append(a)
        q = deque(c for c in range(numCourses) if c not in shouldTakeBefore)

        canTake = 0

        while q:
            cur = q.popleft()
            canTake += 1

            if cur in mightTakeFromHere:
                for nxt in mightTakeFromHere[cur]:
                    shouldTakeBefore[nxt] -= 1
                    if shouldTakeBefore[nxt] == 0:
                        q.append(nxt)
        
        return canTake == numCourses
