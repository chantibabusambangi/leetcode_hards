'''
Given two arrays start[] and end[] such that start[i] is the starting time of ith meeting and end[i] is the ending time of ith meeting. Return the minimum number of rooms required to attend all meetings.
Examples:
Input: start[] = [1, 10, 7], end[] = [4, 15, 10]
Output: 1
Explanation: Since all the meetings are held at different times, it is possible to attend all the meetings in a single room.
'''
#idea is: we use heap for overlapping intervals (it stores all non overlapping intervals and will remove outdated intervals) 
#so the answer was max size of heap on the run time.
def minMeetingRooms(self, start, end):
  intervals=sorted(zip(start,end))
  import heapq
  #idea is we use heapq (if any overlapped interval came, we push that into heapq and outdated inetrvals will be removed)
  if(not intervals):
      return 0
  s,e=intervals[0]
  arr=[[e,s]] #heapq based on endtime #min heap
  res=1 #one room need still now
  for i in range(1,len(intervals)):
      a,b=intervals[i]
      while(arr and arr[0][0]<=a):
          #outdated intervals remove
          heapq.heappop(arr)
      heapq.heappush(arr,[b,a]) #(e,s) to be inserted into heapq
      res=max(res,len(arr))
  return res
