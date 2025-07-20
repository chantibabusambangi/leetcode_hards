'''
Earliest Common Slot
paypal asked this question
Difficulty: MediumAccuracy: 40.4%Submissions: 1K+Points: 4
You are given two lists of availability time slots, slots1 and slots2, for two people. Each slot is represented as [start, end], 
and it is gurranted that within each list, no two slots overlap (i.e., for any two intervals, either start1>end2 or start2>end1). 
Given a metting duration d, return the earliest common time slot of length of least d. If no such slot exits, return an empty array.
Examples:
Input: slots1 = [[10,50], [60,120], [140,210]], slots2 = [[0,15], [60,70]], d = 8
Output: [60,68]
Explanation: The only overlap is [60,70] (10 minutes), which is enough for an 8-minute meeting, so answer is [60,68]
'''
def commonSlot(a, b, d):
  #given two non overlapping intervals
  #find first/earliest overlap intervals (from a,b) st overlap>=d
  #idea: sorting + two pointers
  a.sort()
  b.sort()
  i,j=0,0
  while(i<len(a) and j<len(b)):
      #length of overlap if overlap
      a1,a2=a[i]
      b1,b2=b[j]
      if(not (a1>b2 or b1>a2)): #not (one starts after the other finished)
          x,y=max(a1,b1),min(a2,b2) #overlapping segment [max(a1,b2),min(a2,b2)]
          if(y-x>=d):
              return [x,x+d]
      if(a2>b2): #end times will decide
          j+=1
      else:
          i+=1
  return []
