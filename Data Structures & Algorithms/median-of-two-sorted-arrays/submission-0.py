class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            A, B = nums1, nums2
            total = len(nums1) + len(nums2)
            half = total // 2

            # Step 1: Ensure A is the smaller array to keep the search O(log(min(m,n)))
            if len(B) < len(A):
                A, B = B, A

            l, r = 0, len(A) - 1
                                                                            
            while True:
                                                                                                # i is the partition index for A, j is the partition for B
                i = (l + r) // 2 
                j = half - i - 2 # -2 because of 0-based indexing for both arrays

                                                                                                                                    # Get the values around the partition
                                                                                                                                                # Handle out-of-bounds with -infinity or +infinity
                Aleft = A[i] if i >= 0 else float("-infinity")
                Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
                Bleft = B[j] if j >= 0 else float("-infinity")
                Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

                                                                                                                                                                                                            # Step 2: Check if partition is correct
                if Aleft <= Bright and Bleft <= Aright:
                                                                                                                                                                                                                                        # Odd total: Median is the smallest value of the right half
                    if total % 2:
                        return min(Aright, Bright)
                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                            # Even total: Average of the two middle values
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                    
                elif Aleft > Bright:
                    r = i - 1
                else:
                    l = i + 1