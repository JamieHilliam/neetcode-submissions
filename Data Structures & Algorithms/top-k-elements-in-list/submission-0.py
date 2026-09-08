class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = {}
        for num in nums:
          numFreq[num] = 1 + numFreq.get(num, 0)
        
        mostFreqArr = []
        for i in range(k):
          maxFreq = 0
          maxNum = 0
          for num in nums:
            currentFreq = numFreq.get(num,0)
            if currentFreq > maxFreq and num not in mostFreqArr:
              maxFreq = currentFreq
              maxNum = num
          mostFreqArr.append(maxNum)
        
        return mostFreqArr