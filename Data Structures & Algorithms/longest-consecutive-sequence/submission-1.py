class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak = 1
        current_streak = 1
        seen = set()
        nums.sort()
        if nums == []:
            return 0
        for i in range(1, len(nums)):
            if nums[i] in seen: 
                continue
            seen.add(nums[i])
            if nums[i] == nums[i-1] + 1: 
                current_streak += 1
                continue
            if current_streak > streak:
                streak = current_streak 
            current_streak = 1
        return max(streak,current_streak)

        