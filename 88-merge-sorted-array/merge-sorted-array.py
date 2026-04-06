class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = len(nums1)-1
        len1 = m-1 
        len2 = n-1
        while len2 >= 0  :
            #print(f"{len1} {len2} {index} {nums1}")
            if len1 >=0 and nums1[len1] > nums2[len2] :
                nums1[index] = nums1[len1]
                len1 -= 1
            else :
                nums1[index] = nums2[len2]
                len2 -= 1
            index -= 1
        

        