class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        most_freq = count.most_common()
        result = []
        for i in range(k): 
            result.append(most_freq[i][0])
        return result