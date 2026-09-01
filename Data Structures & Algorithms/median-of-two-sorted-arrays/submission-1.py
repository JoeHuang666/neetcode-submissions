class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A): #make A be the shorter List
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 #mid point of A
            j = half - i - 2 #B's partition len correspond to A's mid

            Aleft = A[i] if i >= 0 else float("-infinity") # To avoid edge case where index is out of bound
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright: #find the right position
                if total % 2: # If total len is odd
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1