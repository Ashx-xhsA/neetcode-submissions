class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def findWholeIsland(i,j):
            directions = [(0,-1),(0,1),(1,0),(-1,0)]
            
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
                return
            if grid[i][j] == "0":
                return 
            if grid[i][j] == "1":
                grid[i][j] = "0"
            
            for m,n in directions:
                findWholeIsland(i+m,j+n)
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                else:
                    findWholeIsland(i,j)
                    res += 1
        return res
        