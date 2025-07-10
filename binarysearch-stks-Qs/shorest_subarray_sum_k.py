'''Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. 
If there is no such subarray, return -1.
A subarray is a contiguous part of an array.
Input: nums = [2,-1,2], k = 3
Output: 3
'''
idea/intuition
#nums can consists of -ves as well (if given only non negatives we can use sliding widnow)
#so here the prefix+deque of  monotonic increasing
def shortestSubarray(self, nums: List[int], k: int) -> int:
  #monotonic queue
  pref=[0]
  for i in range(len(nums)):
      pref.append(pref[-1]+nums[i])
  res=float("inf")
  q=deque([]) #pref[i]-pref[j]>=k means j to i was a valid subarray
  for i in range(len(nums)+1):
      while(q and pref[i]-pref[q[0]]>=k):
          res=min(res,i-q[0])
          q.popleft()
      while(q and pref[q[-1]]>=pref[i]):
          q.pop()
      q.append(i)
  if(res==float("inf")):
      return -1
  return res

 
