class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       m=set(nums)
       if len(nums)!=len(m):
        return True
       else:
        return False
