'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.
Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
  #idea is: use deque remove expired element each time
  #with monotonic decreasing
  res=[]
  q=deque([]) #(val,index) monotonic decreasing q
  for i in range(len(nums)):
      while(q and q[-1][0]<=nums[i]):
          q.pop()  #make monotonic desc q
      q.append((nums[i],i))
      if(i>=k-1):
          res.append(q[0][0])
      if(i-q[0][1]==k-1):
          q.popleft() #expired element
  return res
