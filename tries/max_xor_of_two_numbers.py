'''
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.
Example 1:
Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
'''
#brute force two for loops :O(n2)
#we can use trie whose height was atmost 32, and also finding max xor of any given 'x' can be found in O(32*n)=O(n)
def get_binary(n,M):
    #will give binary string of n in 32 bit representation
    s=bin(n)[2:]
    lead_zeroes=M-len(s)
    return '0'*lead_zeroes+s
class trie_node:
    def __init__(self):
        self.children={}
        self.leaf=False
class trie:
    def __init__(self):
        self.root=trie_node()
    def insert(self,word):
        node=self.root
        for i in word:
            if(i not in node.children):
                node.children[i]=trie_node()
            node=node.children[i]
    def max_xor(self,s,M): # s was binary string #each trie node have atmost two nodes only
        root=self.root
        res=0
        for i in range(M):
            need='1' if(s[i]=='0') else '0'
            if(need in root.children):
                res+=2**(M-i-1)
                root=root.children[need]
            else:
                root=root.children[s[i]]
        return res
trie=trie()
M=max(nums)
bit_len=M.bit_length()
bins=[]
for i in nums:
    s=get_binary(i,bit_len)
    trie.insert(s)
    bins.append(s)
res=0
for s in bins:
    res=max(res,trie.max_xor(s,bit_len))
return res
