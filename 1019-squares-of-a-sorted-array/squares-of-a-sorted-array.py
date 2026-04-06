class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left , right = 0, len(nums)-1
        index = len(nums)-1
        while left <= right :
            mul_left = nums[left]* nums[left]
            mul_right = nums[right]* nums[right]
            if mul_left >=  mul_right:
                result[index] = mul_left
                left +=1
            else:
                result[index] = mul_right
                right -= 1
            index -= 1
            #print(f"{left} {right} {index}")
        return result
