from collections import Counter
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = math.floor((len(nums)/3))
        freq_dict = Counter(nums)
        return [x for x in freq_dict if freq_dict[x] > threshold]