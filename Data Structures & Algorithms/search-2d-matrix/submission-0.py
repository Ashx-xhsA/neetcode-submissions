class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def toNumber(indice):
            colnum = len(matrix[0])
            r = indice // colnum
            c = indice % colnum
            return matrix[r][c]
        l, r = 0, len(matrix) * (len(matrix[0]))
        while l <= r:
            mid = l + (r-l)//2
            midnum = toNumber(mid)
            if midnum < target:
                l = mid +1
            elif midnum > target:
                r = mid -1
            else:
                return True
        return False

        