class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1,nums2
        l,r = 0, len(A)-1
        half = (len(A) + len(B))//2
        while True:
            i = l + (r-l)//2
            j = half -i - 2

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if i < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if j < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if (len(A) + len(B)) % 2:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            else:
                if Aleft > Bright:
                    r = i - 1
                else:
                    l = i + 1
                    

