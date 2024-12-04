class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
      out = []
      num_set = set()
      for num in nums:
        if num not in num_set:
          num_set.add(num)
        else:
          out.append(num)
      return out