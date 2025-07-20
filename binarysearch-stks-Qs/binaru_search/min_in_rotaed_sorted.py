#this can handle duplicates too (yes robustic!)
def findMin(self, nums: List[int]) -> int:
  #binary search
  l, r = 0, len(nums) - 1
  while l < r:
      mid = (l + r) // 2
      if nums[mid] > nums[r]:
          l = mid + 1 #move right
      elif nums[mid] < nums[r]:
          r = mid #move left
      else:
          r -= 1  # handle duplicates safely
  return nums[l]
