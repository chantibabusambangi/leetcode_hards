'''
895. Maximum Frequency Stack
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.
Implement the FreqStack class:
FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
'''
class FreqStack:
    def __init__(self):
        self.freq_stk=defaultdict(list) #freq:[stk]
        self.c=defaultdict(int) #counter
        self.max_freq=0
    def push(self, val: int) -> None:
        f=self.c[val]
        self.freq_stk[f+1].append(val)
        self.c[val]+=1 #update the counter
        self.max_freq=max(self.max_freq,f+1)
    def pop(self) -> int:
        if(self.max_freq==0):
            return -1 #stk was empty
        ans=self.freq_stk[self.max_freq].pop()
        if(not self.freq_stk[self.max_freq]):
            self.max_freq-=1
        self.c[ans]-=1
        return ans
#TC: 1.push:O(1),pop:O(1)
#over all space:O(n) 
