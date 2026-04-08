class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i,num in enumerate(nums) :
            #print(seen)
            if num in seen and abs(seen[num]- i) <= k :
                return True 
            seen[num] = i
        return False

