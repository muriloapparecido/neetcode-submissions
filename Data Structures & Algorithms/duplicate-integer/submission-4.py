class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums): 
            not_seen = nums[i+1:len(nums)]
            if (num in not_seen):
                return True
        return False