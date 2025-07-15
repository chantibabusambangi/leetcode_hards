'''
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] 
such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.
Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
'''
#idea is we use stack and traverse from right to left and keep track of valid (max possible second ) second, when nums[i]<second then 132 was detected.
def find132pattern(self, nums: List[int]) -> bool:
  stk=[]
  second=float("-inf")
  for i in range(len(nums)-1,-1,-1):
      if(nums[i]<second):
          return True
      while(stk and stk[-1]<nums[i]):
          second=stk.pop() #becuse i was there bigger then second
      stk.append(nums[i])
  return False
