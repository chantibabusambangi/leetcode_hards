'''
632. Smallest Range Covering Elements from K Lists
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.
Example 1:
Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
'''
#think off like having only two lists
#idea is we can use two pointers for this tc=0(n+m)
#so back to this problem idea is k pointers and keep track of min and max (we can use heap for this)
a,b=float("-inf"),float("inf")
n=len(nums)
arr=[] #arr[i]=(nums[j],j,i) #at i th position
maxx=nums[0][0]
for i in range(n):
    maxx=max(maxx,nums[i][0])
    heapq.heappush(arr,(nums[i][0],i,0))
while(arr):
    minn,i,j=heapq.heappop(arr)
    if(b-a>maxx-minn):
        a,b=minn,maxx
    if(j<len(nums[i])-1):
        maxx=max(maxx,nums[i][j+1])
        heapq.heappush(arr,(nums[i][j+1],i,j+1))
    else:
        break
return [a,b]
# tc=N*logk (N lenght of shortest list from k lists)
