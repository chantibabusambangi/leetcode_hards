'''
1.N meetings in one room
Difficulty: EasyAccuracy: 45.3%Submissions: 346K+Points: 2Average Time: 20m
You are given timings of n meetings in the form of (start[i], end[i]) where start[i] is the start time of meeting i and end[i] is the finish time of meeting 
i. Return the maximum number of meetings that can be accommodated in a single meeting room,
when only one meeting can be held in the meeting room at a particular time. 
Note: The start time of one chosen meeting can't be equal to the end time of the other chosen meeting.
'''
#idea was greedy sort the intervals based on endtime
intervals=sorted(zip(start,end),key=lambda x:[x[1]])
if(not intervals):
    return 0
s,e=intervals[0] #first interval to do.
res=1 #one meeting was done
for i in range(1,len(intervals)):
    a,b=intervals[i]
    if(a>e):  #here [3,4],[4,10] are said to be overlapped thus why if not we use a>=e
        #we can do this
        s,e=a,b
        res+=1
return res
'''
2.Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest 
of the intervals non-overlapping.
Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.
'''
#idea was same min intervals needed to remove so that rest was non overlapping #one room how mnay intervals we can put (given by above algo right)
#ans = len(intervals)-res #res=max no.of intervals we can put in one room.
#same solution different question.
#greedy was origin for both.
 
