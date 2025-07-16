'''
You are given two 0-indexed arrays nums and cost consisting each of n positive integers.
You can do the following operation any number of times:
Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].
Return the minimum total cost such that all the elements of the array nums become equal.
Example 1:
Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.
'''
#idea: we can use binary search l=min(nums), r=max(nums)
#this follows the convex property if(cost for (mid))<cost for (mid+1) : then on right half cost was increasing spo move left r=mid-1 else:move right l=mid+1
#bianry search
n=len(nums)
l=min(nums) #best case equal array
r=max(nums) #worst case
def find_cost(mid):
    c=0
    for i in range(len(nums)):
        diff=abs(nums[i]-mid)
        c+=diff*cost[i]
    return c
res=float("inf")
while(r>=l):
    mid=(l+r)//2
    mid_cost,prev_cost=find_cost(mid),find_cost(mid+1)
    if(mid_cost<prev_cost):
        res=min(res,mid_cost)
        r=mid-1
    else:
        res=min(res,prev_cost)
        l=mid+1
return res
