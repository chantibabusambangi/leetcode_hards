'''
301. Remove Invalid Parentheses
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.
Example 1:
Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"] 
'''
#idea is we use prunning and bfs(using what? using invalid open,closed parenthesis)
#open,close can get using a stack.(#prerequsite: valid parenthesis leetcode:125)
def removeInvalidParentheses(self, s: str) -> List[str]:
  #explore all the ways buddy.
  res=set()
  def bfs(sol,i,openn,close,open_count):
      if(i==len(s)):
          if(openn==0 and close==0 and open_count==0):
              res.add(sol)
          return 
      if(s[i]=='('):
          if(openn>0):
              bfs(sol,i+1,openn-1,close,open_count)
          bfs(sol+'(',i+1,openn,close,open_count+1)
      elif(s[i]==')'):
          if(close>0): #open_count validates the string
              bfs(sol,i+1,openn,close-1,open_count) #dont pick
          if(open_count>0):
              bfs(sol+')',i+1,openn,close,open_count-1)
      else:
          bfs(sol+s[i],i+1,openn,close,open_count)
  #use stack to find inbalanced open and close brackets
  stk=[]
  for i in range(len(s)):
      if(s[i]=='('):
          stk.append(s[i])
      elif(s[i]==')'):
          if(stk and stk[-1]=='('):
              stk.pop()
          else:
              stk.append(')')
  openn,close=stk.count('('),stk.count(')')
  bfs("",0,openn,close,0)
  return list(res)
  #TC: O(2^n) in worst case
  #space: O(2^r) r=invalid parenthesis count
  #please fell free to ask any questions or any kind of reach outs.
