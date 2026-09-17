from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Key is set and value is list
        anagrams = defaultdict(list)
        for curr in strs:
            key = tuple(sorted(curr))
            anagrams[key].append(curr)
        return list(anagrams.values())