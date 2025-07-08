'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:
MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
'''
#app1 using sortedcontainers.SortedList
class MedianFinder:
    from sortedcontainers import SortedList
    def __init__(self):
        self.arr=SortedList()
    def addNum(self, num: int) -> None:
        self.arr.add(num)
    def findMedian(self) -> float:
        n=len(self.arr)
        if(n%2==0):
            n1,n2=self.arr[n//2],self.arr[n//2-1]
            return (n1+n2)/2
        return self.arr[n//2]
TC:addNum: O(logn), findMedian: O(1)
space:O(n)
#app2 using two heaps
#only thing is:1. all elements in min greater than all elements in max heap and 2.balance
def __init__(self):
    self.min=[]
    self.max=[]
def addNum(self, num: int) -> None:
    if(len(self.min)>len(self.max)):
        heapq.heappush(self.max,-1*num)
    else:
        heapq.heappush(self.min,num) #this ensures balance of sizes
    while(self.min and self.max and self.min[0]<-1*self.max[0]): #this ensure min heap holds top half and bottom elements hold by max hea(smaller half)
        a,b=-1*heapq.heappop(self.max),heapq.heappop(self.min)
        heapq.heappush(self.max,-1*b)
        heapq.heappush(self.min,a)
def findMedian(self) -> float:
    if(len(self.min)==len(self.max)):
        return (self.min[0]+-1*self.max[0])/2
    return self.min[0] 
