class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        most_freq = nums_counter.most_common()
        result = []
        for i in range(0,k):
            result.append(most_freq[i][0])

        return result
        