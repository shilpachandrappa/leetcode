class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_num = 9999999
        index =0
        for num in nums :
            if prev_num != num :
                prev_num = num
                nums[index] = num
                index += 1
                #print(nums)
        return index