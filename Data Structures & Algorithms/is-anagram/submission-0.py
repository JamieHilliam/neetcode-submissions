class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
          return False
        
        sDict = {}
        tDict = {}
        for char in s:
          sDict[char] = 1 + sDict.get(char, 0)
        
        for char in t:
          tDict[char] = 1 + tDict.get(char, 0)
        
        return sDict == tDict