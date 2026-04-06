class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = Counter(nums1)
        result = []
        for num in nums2 :
            if mapping[num] > 0 :
                result.append(num)
                mapping[num] -= 1
        return result