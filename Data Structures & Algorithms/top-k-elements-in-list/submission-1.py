from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        sorted_freq = sorted(freq_dict, key = lambda x: freq_dict[x])
        top_k = []
        for i in range(1,k+1):
            top_k.append(sorted_freq[-i])
        return top_k