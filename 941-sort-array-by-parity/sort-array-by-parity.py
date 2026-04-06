class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = 0
        odd = len(nums)-1
        res= [0] * len(nums)
        for num in nums :
            if num%2 == 0 :
                res[even] = num
                even += 1
            else :
                res[odd] = num
                odd -= 1
        return res