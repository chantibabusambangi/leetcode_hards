'''
891. Sum of Subsequence Widths
The width of a sequence is the difference between the maximum and minimum elements in the sequence.
Given an array of integers nums, return the sum of the widths of all the non-empty subsequences of nums. Since the answer may be very large, return it modulo 109 + 7.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
Example 1:
Input: nums = [2,1,3]
Output: 6
Explanation: The subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.
'''
#brute force is (dont take all subsequences and add range to res)
#idea1 (O(n2) approach) is sort the nums and find the range between nums[i],nums[j] j>i and this sequence can appears for 2**(j-i-1) times right
nums.sort()
res=0
MOD=10**9+7
for i in range(len(nums)-1):
  for j in range(i+1,len(nums)):
      width=2**(j-i-1)
      ran=nums[j]-nums[i] #range
      res+=width*ran
      res=res%MOD
res=res%MOD
return res
#but this can get you TLE O(n2)
#we can do better 
#after sorting 
#each nums[i] can contribute as max for (i) elements i.e 2**(i) subsequences can possible right
#and on right n-i-1 elements are there for them nums[i] act as min i.e 2**(n-i-1) subsequences
nums.sort()
MOD=10**9+7
res=0
power={0:1} #2**i
for i in range(1,len(nums)):
  power[i]=power[i-1]*2
  power[i]=power[i]%MOD
for i in range(len(nums)):
  ans=power[i]-power[len(nums)-i-1]
  ans*=nums[i]
  res+=ans
  res=res%MOD
res=res%MOD
return res
#tc=O(n) only
