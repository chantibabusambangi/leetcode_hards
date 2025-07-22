'''
Given a sorted integer array nums and an integer n, add/patch elements to the array such that 
any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.
Return the minimum number of patches required.
Example 1:
Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
'''
#idea is greedy algorithm will work because we start with missing=1 it take care of any missing sum
def minPatches(self, nums: List[int], n: int) -> int:
  res=0
  #a number a formed from it self or sum of numbers lower than it.
  missing=1
  i=0
  while(missing<=n):
      if(i<len(nums) and nums[i]<=missing):
          missing+=nums[i]
          i+=1
      else:
          missing+=missing
          res+=1
  return res
