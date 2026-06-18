class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        streak = set()
        best = 0
        if nums == []: 
            return 0
        for i in range(1, len(nums)):
            if nums[i] in streak:
                continue
            if nums[i] == nums[i-1] + 1:
                streak.add(nums[i])
            else: 
                if len(streak) + 1 > best: 
                    best = len(streak) + 1
                print(streak)
                streak.clear()


        return max(best,len(streak) + 1)