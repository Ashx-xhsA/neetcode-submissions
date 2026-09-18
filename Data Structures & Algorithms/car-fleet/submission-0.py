# from the furthest to closest, iterate to see if it collide with the latter one. if so, they form a cat fleet. and we abandon the closer one to only consider the further one
# if they does not collide,we consider them two car fleet
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carData = [[p,s] for p,s in zip(position,speed)]
        carData.sort()
        stk = []
        for i in range(len(position)-1,-1,-1):
            p = carData[i][0]
            s = carData[i][1]
            arriveAt = (target - p)/s
            if not stk:
                stk.append(arriveAt)
            else:
                if arriveAt > stk[-1]:
                    stk.append(arriveAt)
        return len(stk)
                    


        