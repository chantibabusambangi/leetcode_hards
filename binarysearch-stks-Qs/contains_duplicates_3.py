'''
You are given an integer array nums and two integers indexDiff and valueDiff.
Find a pair of indices (i, j) such that:
i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.
Example 1:
Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
'''
#idea is binarysearch+slidingwindow
def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
  #bianry search+sliding window
  def floor(nums,x):
      if(not nums or nums[0]>x):
          return float("inf")
      l,r=0,len(nums)-1
      res=-1
      while(r>=l):
          mid=(l+r)//2
          if(nums[mid]<=x):
              res=nums[mid]
              l=mid+1
          else:
              r=mid-1
      return res
  def ceil(nums,x):
      if(not nums or nums[-1]<x):
          return float("inf")
      l,r=0,len(nums)-1
      res=-1
      while(r>=l):
          mid=(l+r)//2
          if(nums[mid]>=x):
              res=nums[mid]
              r=mid-1
          else:
              l=mid+1
      return res
  from sortedcontainers import SortedList
  if(k<=0 or t<0):
      return False
  arr=SortedList([nums[0]])
  for i in range(1,len(nums)):
      c=ceil(arr,nums[i])
      f=floor(arr,nums[i])
      if (c!=float("inf")  and c - nums[i] <= t) or (f!=float("inf") and nums[i]-f<=t):
          return True
      arr.add(nums[i])
      if(i>=k):
          arr.remove(nums[i-k]) #remove element that expires
  return False
     
