class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        write_index = 0
        for num , count in num_count.items():
            for _ in range(min(2,count)):
                nums[write_index] = num
                write_index += 1
        return write_index