'''You are given an integer array of unique positive integers nums. Consider the following graph:
There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.
ex.1
Input: nums = [4,6,15,35]
Output: 4
'''
#idea is use :union find connect number with all its prime factors
def largestComponentSize(self, nums: List[int]) -> int:
  from collections import defaultdict
  parent = {}
  def find(x):
      if parent.setdefault(x, x) != x:
          parent[x] = find(parent[x])
      return parent[x]
  def union(x, y):
      parent[find(x)] = find(y)
  def get_factors(num): #WILL give prime factors
      i = 2
      factors = set()
      while i * i <= num:
          if num % i == 0:
              factors.add(i)
              while num % i == 0:
                  num //= i
          i += 1
      if num > 1:
          factors.add(num)
      return factors
  for num in nums:
      for factor in get_factors(num):
          union(num, factor)
  count = defaultdict(int)
  max_size = 0
  for num in nums:
      root = find(num)
      count[root] += 1
      max_size = max(max_size, count[root])
  return max_size
