'''
**WORD BREAK-1**
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
'''
#idea is we use dp, dp[i] represents the bool either true(can be segmented) or False(cannot break)
#dp[i]=True if any j such that dp[j-1] was True and s[j:i] is the word that exist.
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
  n=len(s)
  h=set(words)
  M=0
  for i in words:
      M=max(M,len(i))
  dp=[[] for i in range(n)]
  for i in range(len(s)):
      for j in range(i,max(i-M,-1),-1):
          if(s[j:i+1] in h):
              if(j==0):
                  dp[i].append(s[j:i+1])
                  continue
              for strs in dp[j-1]:
                  dp[i].append(strs+' '+s[j:i+1])
  return dp[-1]
'''
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
'''
#here you need all the segmented strings that form s.
#here dp[i] should  store list of strings that form segmentation of s[:i] till i.
#eventually we return dp[-1] #which gives the segmentation strings of s.
def wordBreak(self, s: str, words: List[str]) -> List[str]:
  #same as word break 1
  n=len(s)
  h=set(words)
  M=0
  for i in words:
      M=max(M,len(i))
  dp=[[] for i in range(n)]
  for i in range(len(s)):
      for j in range(i,max(i-M,-1),-1):
          if(s[j:i+1] in h):
              if(j==0):
                  dp[i].append(s[j:i+1])
                  continue
              for strs in dp[j-1]:
                  dp[i].append(strs+' '+s[j:i+1])
  return dp[-1]
